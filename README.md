DocuQuery API

This project is a simple document-based question answering API built with Python and FastAPI.Users can upload documents, and the system allows questions to be asked based only on the uploaded content. The goal is to show how document search and AI-based answering can be combined in a clean backend service.

What it does

Upload text documents through an APISplit documents into smaller chunks
Convert chunks into vector embeddingsStore embeddings using FAISS for fast search
Find relevant contentfor a question
Generate an answer using an LLM based on that content

Tech stack

Python 3
FastAPI
FAISS (vector search)
OpenAI embeddings and GPT model

FAISS is used to avoid slow brute-force searching and make the system scalable.

API endpoints

POST /documents – upload and index documents
POST /query – ask questions using indexed documents
GET /documents – list uploaded documents
DELETE /documents/{id} – remove a document

Running the project

pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key"
uvicorn app.main:app --reload --port 8001


Open:

http://127.0.0.1:8001/docs