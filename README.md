# 📚 RAG Chatbot — AI Document Q&A

A simple Retrieval-Augmented Generation (RAG) application that lets you upload a PDF and ask questions about its content. Built with a full RAG pipeline: PDF ingestion → semantic chunking → vector search → LLM generation.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)](https://langchain.com)
[![MistralAI](https://img.shields.io/badge/Mistral_AI-FF7000?logoColor=white)](https://mistral.ai)

---

## How It Works

```
PDF Upload → Text Chunking → HuggingFace Embeddings → ChromaDB
                                                           ↓
                  User Question → MMR Retrieval (top-4 chunks) → Mistral AI → Answer
```

- **Chunking** — `RecursiveCharacterTextSplitter` with 1000-char chunks and 200-char overlap
- **Embeddings** — `BAAI/bge-small-en-v1.5` via HuggingFace (runs locally, no API cost)
- **Retrieval** — Maximal Marginal Relevance (MMR) for diverse, non-redundant context
- **Generation** — `mistral-small-latest` with a strict context-only system prompt

---

## Features

- Upload any PDF — textbooks, research papers, reports
- Grounded answers — model is instructed to answer only from document context
- MMR retrieval — avoids redundant chunks, improves answer quality
- Persistent vector store — ChromaDB saves embeddings between sessions
- Chat history — full conversational memory within the session

---

## Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| PDF Loading | LangChain `PyPDFLoader` |
| Text Splitting | LangChain `RecursiveCharacterTextSplitter` |
| Embeddings | HuggingFace `BAAI/bge-small-en-v1.5` |
| Vector DB | ChromaDB (local, persistent) |
| LLM | Mistral AI (`mistral-small-latest`) |

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/OmmTripathy/RAG_Chatbot.git
cd RAG_Chatbot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**
```bash
cp .env.example .env
# Open .env and add your Mistral API key
```

```env
MISTRAL_API_KEY=your_key_here
```

**4. Run**
```bash
streamlit run app.py
```

App opens at `http://localhost:8501`

---

## Project Structure

```
RAG_Chatbot/
├── app.py              # Main application — full RAG pipeline
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore
└── README.md
```

---

## Limitations & Planned Improvements

| Current | Planned |
|---|---|
| Single PDF per session | Multi-PDF support |
| No source citation | Display page numbers with each answer |
| In-memory chat history | Persistent chat history across sessions |
| PDF only | Support DOCX, TXT, web URLs |

---

## Author

**Omm Kishor Tripathy** — [LinkedIn](https://linkedin.com/in/ommtripathy) · [GitHub](https://github.com/OmmTripathy)
