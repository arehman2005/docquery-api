import faiss
import numpy as np

DIMENSION = 1536  # OpenAI embedding size
index = faiss.IndexFlatL2(DIMENSION)

vectors = []
metadata = []

def add_vector(embedding, meta):
    vectors.append(embedding)
    metadata.append(meta)
    index.add(np.array([embedding]).astype("float32"))

def search_vectors(query_embedding, top_k=3):
    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"), top_k
    )

    results = []
    for i in indices[0]:
        if i != -1:
            results.append(metadata[i])
    return results
