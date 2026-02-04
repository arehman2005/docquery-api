from fastapi import FastAPI, HTTPException
from app.schemas import DocumentList, QueryRequest
from app.store import add_document, get_documents, delete_document
from app.query import answer_question

app = FastAPI(title="DocuQuery API")

@app.get("/")
def root():
    return {"message": "DocuQuery API is running"}

@app.post("/documents")
def upload_documents(payload: DocumentList):
    ids = []
    for doc in payload.documents:
        doc_id = add_document(doc.title, doc.content)
        ids.append(doc_id)

    return {
        "message": "Documents added successfully",
        "document_ids": ids
    }

@app.get("/documents")
def list_documents():
    return get_documents()

@app.delete("/documents/{doc_id}")
def remove_document(doc_id: str):
    success = delete_document(doc_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted successfully"}

@app.post("/query")
def query_docs(payload: QueryRequest):
    return answer_question(payload.question)
