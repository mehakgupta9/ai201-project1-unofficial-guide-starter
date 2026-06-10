import os
from dotenv import load_dotenv
from groq import Groq
from retrieval import retrieve

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask(question):
    retrieved_chunks = retrieve(question, top_k=4, print_results=False)

    context_parts = []
    sources = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        source = chunk["source"]
        text = chunk["text"]

        context_parts.append(f"[Source {i}: {source}]\n{text}")
        sources.append(source)

    context = "\n\n".join(context_parts)

    prompt = f"""
You are answering questions for an unofficial UMD CS guide.

Answer the user's question using ONLY the provided retrieved context.
Do not use outside knowledge.
If the context does not contain enough information, say:
"I don't have enough information in the collected documents to answer that."

Question:
{question}

Retrieved context:
{context}

Write a clear answer and mention the source filenames used.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    unique_sources = sorted(set(sources))

    return {
        "answer": answer,
        "sources": unique_sources,
        "chunks": retrieved_chunks
    }


if __name__ == "__main__":
    while True:
        question = input("\nAsk a question: ")

        if question.lower() in ["exit", "quit"]:
            break

        result = ask(question)

        print("\nAnswer:")
        print(result["answer"])

        print("\nSources:")
        for source in result["sources"]:
            print("-", source)
