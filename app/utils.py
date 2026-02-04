# app/utils.py

import os
import math
from openai import OpenAI

# Initialize OpenAI client (API key must be in env variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chunk_text(text: str, chunk_size: int = 300):
    """
    Split text into smaller chunks for embeddings
    """
    words = text.split()
    chunks = []

    current_chunk = []
    current_length = 0

    for word in words:
        current_length += len(word)

        if current_length > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0

        current_chunk.append(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def get_embedding(text: str):
    """
    Generate vector embedding for a text chunk
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def cosine_similarity(vec1, vec2):
    """
    Compute cosine similarity between two vectors
    """
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot_product / (norm1 * norm2)
