from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from app.services.document_processor import DocumentProcessor
from app.services.ai_engine import ai_engine
from pydantic import BaseModel

api_router = APIRouter()

class ChatPayload(BaseModel):
    doc_id: str
    question: str

@api_router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_path = await DocumentProcessor.save_upload(file)
        raw_text = await DocumentProcessor.extract_text(file_path)
        doc_id = os.path.basename(file_path)
        chunks = ai_engine.chunk_text(raw_text)
        ai_engine.create_vector_store(doc_id, chunks)
        summary = ai_engine.generate_summary(raw_text)
        return {"doc_id": doc_id, "filename": file.filename, "summary": summary, "status": "Ready"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/chat")
async def chat_with_document(payload: ChatPayload):
    answer = ai_engine.generate_answer(payload.doc_id, payload.question)
    return {"answer": answer}