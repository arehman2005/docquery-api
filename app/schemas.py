from pydantic import BaseModel
from typing import List

class Document(BaseModel):
    title: str
    content: str

class DocumentList(BaseModel):
    documents: List[Document]

class QueryRequest(BaseModel):
    question: str
