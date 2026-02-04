from openai import OpenAI
from app.store import chunks_store
from app.utils import get_embedding, cosine_similarity

client = OpenAI()

def answer_question(question: str):
    if not chunks_store:
        return {
            "answer": "No documents available to search.",
            "sources": []
        }

    question_embedding = get_embedding(question)

    scored_chunks = []
    for chunk in chunks_store:
        if "embedding" not in chunk:
            continue
        score = cosine_similarity(question_embedding, chunk["embedding"])
        scored_chunks.append((score, chunk))

    if not scored_chunks:
        return {
            "answer": "No relevant information found.",
            "sources": []
        }

    top_chunks = sorted(scored_chunks, key=lambda x: x[0], reverse=True)[:3]

    context = "\n\n".join(chunk["text"] for _, chunk in top_chunks)

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": [
            {"doc_id": c["doc_id"], "title": c["title"]}
            for _, c in top_chunks
        ]
    }
