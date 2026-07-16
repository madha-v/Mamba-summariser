import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class AIEngine:
    def __init__(self, model_tag="state-spaces/mamba-130m-hf", embed_tag="BAAI/bge-small-en-v1.5"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_tag)
        self.model = AutoModelForCausalLM.from_pretrained(model_tag).to(self.device)
        self.embed_model = SentenceTransformer(embed_tag, device=self.device)
        self.vector_indices = {}

    def chunk_text(self, text: str, max_chars: int = 1500, overlap: int = 200) -> list:
        chunks = []
        start = 0
        while start < len(text):
            end = start + max_chars
            chunks.append(text[start:end])
            start += max_chars - overlap
        return chunks

    def create_vector_store(self, doc_id: str, chunks: list):
        embeddings = self.embed_model.encode(chunks, convert_to_numpy=True)
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        self.vector_indices[doc_id] = {"index": index, "chunks": chunks}

    def query_vector_store(self, doc_id: str, query: str, top_k: int = 3) -> str:
        if doc_id not in self.vector_indices: return ""
        meta = self.vector_indices[doc_id]
        query_vector = self.embed_model.encode([query], convert_to_numpy=True)
        _, indices = meta["index"].search(query_vector, top_k)
        return "\n".join([meta["chunks"][i] for i in indices[0] if i != -1])

    def generate_summary(self, text: str) -> str:
        chunks = self.chunk_text(text, max_chars=2000)
        input_text = f"Summarize this document content accurately:\n\n{chunks[0]}\n\nSummary:"
        inputs = self.tokenizer(input_text, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=150)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).replace(input_text, "").strip()

    def generate_answer(self, doc_id: str, question: str) -> str:
        context = self.query_vector_store(doc_id, question)
        if not context: return "Document context not found or not indexed."
        input_text = f"Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer strictly from context:"
        inputs = self.tokenizer(input_text, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=100)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).replace(input_text, "").strip()

ai_engine = AIEngine()