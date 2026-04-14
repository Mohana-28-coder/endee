# 🤖 AI Learning Path Recommender (Endee + Semantic Search)

## 📌 Overview
This project is an AI/ML-based learning recommendation system that suggests study topics based on user input using semantic search with a vector database (Endee).

---

## 🧠 Tech Stack
- Python
- Endee Vector Database
- Sentence Transformers (MiniLM embeddings)

---

## ⚙️ How It Works

1. Convert learning topics into embeddings
2. Store embeddings in Endee vector database
3. Convert user query into embedding
4. Perform semantic similarity search
5. Return most relevant learning topics

---

## 🔍 Features
- AI-based semantic search (not keyword matching)
- Vector database storage using Endee
- Intelligent learning path recommendations
- RAG-style retrieval foundation

---

## 🚀 Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
