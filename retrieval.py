import chromadb
from sentence_transformers import SentenceTransformer
from pipeline import load_documents, chunk_document, RAW_DIR

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "unofficial_guide"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 4


def build_vector_store():
    model = SentenceTransformer(EMBEDDING_MODEL)

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    # Delete old collection so you do not duplicate chunks
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    documents = load_documents(RAW_DIR)

    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc)
        all_chunks.extend(chunks)

    print(f"Loaded {len(documents)} documents.")
    print(f"Created {len(all_chunks)} chunks.")

    for i, chunk in enumerate(all_chunks):
        embedding = model.encode(chunk["text"]).tolist()

        collection.add(
            ids=[f"chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[{
                "source": chunk["source"],
                "chunk_index": i,
                "word_count": chunk["word_count"]
            }]
        )

    print(f"Stored {len(all_chunks)} chunks in ChromaDB.")


def retrieve(query, top_k=TOP_K, print_results=True):
    model = SentenceTransformer(EMBEDDING_MODEL)

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_collection(name=COLLECTION_NAME)

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved_chunks = []

    for i in range(len(results["documents"][0])):
        document = results["documents"][0][i]
        metadata = results["metadatas"][0][i]
        distance = results["distances"][0][i]

        chunk = {
            "text": document,
            "source": metadata["source"],
            "chunk_index": metadata["chunk_index"],
            "word_count": metadata["word_count"],
            "distance": distance
        }

        retrieved_chunks.append(chunk)

        if print_results:
            print(f"\nResult {i + 1}")
            print(f"Source: {metadata['source']}")
            print(f"Chunk index: {metadata['chunk_index']}")
            print(f"Distance: {distance:.4f}")
            print("-" * 80)
            print(document)

    return retrieved_chunks


def main():
    build_vector_store()

    test_queries = [
        "Which CMSC course was most frequently mentioned as difficult in the Reddit discussion about the hardest undergraduate CS classes?",
        "What study advice do multiple students give for succeeding in Nelson Padua-Perez's CMSC131 and CMSC132 courses?",
        "Which professor was recommended for undergraduate students interested in cybersecurity research?"]

    for query in test_queries:
        retrieve(query)


if __name__ == "__main__":
    main()
