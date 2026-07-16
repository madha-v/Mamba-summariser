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





The backend will be live at http://localhost:8000. You can view the interactive API docs at http://localhost:8000/docs.2. Frontend Setup (Coming Soon)Once the frontend directory is established, run the following commands to spin up the UI:Bashcd frontend
npm install
npm run dev
The React workspace will be accessible at http://localhost:3000 or http://localhost:5173.📡
 Core API EndpointsMethodEndpointDescription
GET/api/v1/healthSystem operational health check.
POST/api/v1/uploadUploads a document, extracts text, generates embeddings, and returns a summary.
POST/api/v1/chatQueries the vector database to answer questions specifically grounded in the uploaded document.

🧠 Why Mamba?Standard Transformers scale quadratically ($O(N^2)$) with sequence length, making long documents computationally expensive. State Space Models like Mamba scale linearly ($O(N)$), providing equivalent or superior reasoning capabilities while using a fraction of the memory.

This allows MambaDoc AI to process 500+ page PDFs quickly and efficiently on consumer hardware.

📝 LicenseThis project is licensed under the MIT License - see the LICENSE file for details.
