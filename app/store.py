import uuid
from app.utils import chunk_text, get_embedding

documents = {}
chunks_store = []


def add_document(title: str, content: str):
    doc_id = str(uuid.uuid4())

    documents[doc_id] = {
        "id": doc_id,
        "title": title,
        "content": content
    }

    for chunk in chunk_text(content):
        chunks_store.append({
            "doc_id": doc_id,
            "title": title,
            "text": chunk,
            "embedding": get_embedding(chunk)
        })

    return doc_id


def get_documents():
    return list(documents.values())


def delete_document(doc_id: str) -> bool:
    if doc_id not in documents:
        return False

    del documents[doc_id]
    global chunks_store
    chunks_store = [c for c in chunks_store if c["doc_id"] != doc_id]
    return True
