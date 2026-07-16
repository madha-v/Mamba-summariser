import os
import uuid
from fastapi import UploadFile
import pdfplumber
from docx import Document
from app.config.config import settings

class DocumentProcessor:
    @staticmethod
    async def save_upload(file: UploadFile) -> str:
        file_ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(settings.UPLOAD_DIR, unique_filename)
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        return file_path

    @classmethod
    async def extract_text(cls, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".pdf":
            extracted_text = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text: extracted_text.append(text)
            return "\n\n".join(extracted_text)
        elif ext in [".docx", ".doc"]:
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        elif ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        raise ValueError("Unsupported format.")