# Mamba-summariser
Smart Document Summarizer using Mamba better to using tranformers
# 🐍📄 MambaDoc AI

**Intelligent Document Summarizer & Contextual Chat Engine using Mamba State Space Models.**

MambaDoc AI is a high-performance, full-stack application designed to process, summarize, and query long-form documents. By leveraging the linear-time sequence scaling of **Mamba State Space Models (SSMs)**, this project overcomes the context-window limitations and computational bottlenecks of traditional Transformer-based LLMs, making it capable of parsing massive documents efficiently.

---

## ✨ Key Features

*   **Long-Document Summarization:** Powered by Mamba SSMs to handle large files seamlessly.
*   **Intelligent Extraction & OCR:** Extracts text natively from PDFs, DOCX, and TXT files, with automatic fallback to PaddleOCR for scanned documents.
*   **Retrieval-Augmented Generation (RAG):** Contextually grounds AI chat responses to your uploaded documents using FAISS vector search and dense embeddings.
*   **Dynamic Document Chunking:** Smart text overlapping to preserve contextual integrity during embedding.
*   **Modern Workspace UI:** A sleek, responsive React dashboard built with Tailwind CSS.

---

## 🛠️ Tech Stack

**Backend (Processing & AI):**
*   **Framework:** FastAPI, Uvicorn
*   **AI/ML:** PyTorch, Hugging Face Transformers, `mamba-ssm`
*   **Vector Search:** FAISS, Sentence-Transformers (BGE Embeddings)
*   **Document Parsing:** `pdfplumber`, `python-docx`, PaddleOCR

**Frontend (UI & Interaction):**
*   **Framework:** React (TypeScript)
*   **Styling:** TailwindCSS
*   **State Management:** React Hooks

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   *Optional:* CUDA-compatible GPU (for native Mamba speed, though CPU fallback is configured).

### 1. Backend Setup

Navigate to the backend directory, install the required packages, and start the FastAPI server:

```bash
cd backend

# (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn app.main:app --reload --port 8000
