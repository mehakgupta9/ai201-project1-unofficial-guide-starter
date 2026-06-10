import os
import re
import html
import random

RAW_DIR = "documents"

MIN_WORDS = 25
MAX_WORDS = 180
OVERLAP_WORDS = 30


def load_documents(raw_dir):
    documents = []

    for filename in os.listdir(raw_dir):
        if filename.endswith(".txt"):
            path = os.path.join(raw_dir, filename)

            with open(path, "r", encoding="utf-8") as file:
                text = file.read()

            documents.append({
                "filename": filename,
                "text": text
            })

    return documents


def clean_text(text):
    text = html.unescape(text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_long_section(text):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + MAX_WORDS
        chunk = " ".join(words[start:end])

        if len(chunk.split()) >= MIN_WORDS:
            chunks.append(chunk)

        start += MAX_WORDS - OVERLAP_WORDS

    return chunks


def split_into_sections(text):
    """
    Keeps full reviews/comments/replies together instead of splitting badly.
    """
    pattern = r"(?=(?:Comment \d+ by|Reply by|Review \d+|Original Post by|Original Post:))"
    sections = re.split(pattern, text)

    cleaned_sections = []

    for section in sections:
        section = clean_text(section)

        if len(section.split()) >= MIN_WORDS:
            cleaned_sections.append(section)

    return cleaned_sections


def chunk_document(document):
    sections = split_into_sections(document["text"])
    chunks = []

    for section in sections:
        word_count = len(section.split())

        if word_count <= MAX_WORDS:
            chunks.append({
                "source": document["filename"],
                "text": section,
                "word_count": word_count
            })
        else:
            split_chunks = split_long_section(section)

            for chunk in split_chunks:
                chunks.append({
                    "source": document["filename"],
                    "text": chunk,
                    "word_count": len(chunk.split())
                })

    return chunks


def main():
    documents = load_documents(RAW_DIR)

    print(f"Loaded {len(documents)} documents.")

    all_chunks = []

    for doc in documents:
        chunks = chunk_document(doc)
        all_chunks.extend(chunks)

    print(f"Created {len(all_chunks)} chunks.")

    print("\nPrinting 5 sample chunks:\n")

    sample_chunks = random.sample(all_chunks, min(5, len(all_chunks)))

    for i, chunk in enumerate(sample_chunks, start=1):
        print("=" * 80)
        print(f"Chunk {i}")
        print(f"Source: {chunk['source']}")
        print(f"Word count: {chunk['word_count']}")
        print("-" * 80)
        print(chunk["text"])
        print()

    return all_chunks


if __name__ == "__main__":
    main()
