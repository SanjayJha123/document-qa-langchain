# 📄 Document Q&A Assistant

A powerful, lightweight web app that lets you upload documents (PDF, DOCX, TXT), ask questions in natural language, and get accurate answers grounded in your content — powered by **LangChain**, **FAISS**, and **OpenAI**.

![LangChain + FAISS + OpenAI](https://img.shields.io/badge/RAG-LangChain-blue?logo=OpenAI)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)
![License](https://img.shields.io/github/license/SanjayJha123/document-qa-langchain)

---

## 🚀 Features

- ✅ Upload multiple document formats (PDF, DOCX, TXT)
- ✂️ Automatic chunking and embedding
- 🔍 Semantic search using FAISS
- 🧠 LLM-powered question answering
- 📚 Source content shown for every answer
- 🧪 Easy to extend with Bedrock, ChromaDB, OpenSearch

---

## 🖼️ Demo

![Demo Screenshot](demo/demo.png) <!-- You can upload a screenshot here -->

---

## 🧰 Tech Stack

| Layer         | Tool/Library         |
|---------------|----------------------|
| UI            | Streamlit            |
| Embeddings    | OpenAI / Bedrock     |
| Vector Store  | FAISS (local)        |
| Q&A Engine    | LangChain            |
| Parsing       | PyMuPDF, python-docx |
| Language Model| OpenAI GPT-4         |

---

## 📂 Project Structure

```bash
document-qa-langchain/
├── app.py              # Streamlit frontend
├── ingest.py           # Document loading, chunking, embedding
├── qa_chain.py         # LangChain Q&A pipeline
├── utils.py            # Optional helpers
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── data/
    ├── uploads/        # Uploaded documents
    └── vectorstore/    # FAISS vector index


