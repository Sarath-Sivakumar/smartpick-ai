# 📱 SmartPick AI

SmartPick AI is a semantic smartphone recommendation engine built to learn the foundations of Retrieval-Augmented Generation (RAG), embeddings, and AI-powered search systems.

Unlike traditional keyword-based search, SmartPick AI uses sentence embeddings and similarity matching to understand user intent and recommend the most relevant smartphones based on requirements such as gaming, camera quality, battery life, performance, and budget.

---

## 🚀 Features

* Semantic smartphone search using embeddings
* Retrieval-based recommendation engine
* FastAPI-powered REST API
* Cosine similarity ranking
* Structured recommendation generation
* Foundation for future RAG and LLM integration

---

## 🏗️ Architecture

```text
User Query
    ↓
Embedding Generation
    ↓
Similarity Search
    ↓
Phone Ranking
    ↓
Recommendation Generator
    ↓
API Response
```

### Example Flow

```text
Best gaming phone under ₹35,000
            ↓
Convert query to embedding
            ↓
Compare against phone embeddings
            ↓
Rank phones by similarity
            ↓
Generate recommendations
```

---

## 📂 Project Structure

```text
smartpick-ai/
│
├── app/
│   ├── main.py
│   ├── retriever.py
│   └── generator.py
│
├── models/
│   └── request.py
│
├── data/
│   └── phones.json
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

### Backend

* Python
* FastAPI
* Pydantic

### AI Components

* Sentence Transformers
* Embeddings
* Cosine Similarity
* Semantic Search

### Dataset

* JSON-based smartphone knowledge base

---

## 🧠 AI Concepts Implemented

### Embeddings

Each smartphone specification is converted into a numerical vector representation using a Sentence Transformer model.

Example:

```text
"Excellent gaming phone"
```

and

```text
"Best phone for BGMI"
```

generate similar vector representations despite using different words.

---

### Semantic Search

Instead of searching for exact keywords, SmartPick AI searches based on meaning.

Traditional Search:

```text
gaming phone
```

matches only:

```text
gaming
```

Semantic Search:

```text
gaming phone
```

can match:

```text
performance phone
BGMI phone
high FPS smartphone
```

---

### Retrieval Engine

The retriever:

1. Converts the query into an embedding
2. Computes similarity scores
3. Ranks phones
4. Returns top matches

---

### Recommendation Generator

The generator transforms retrieved smartphone data into structured recommendations that can be consumed by clients or future LLM-powered systems.

---

## 🔍 API Endpoint

### Recommend Smartphones

**POST**

```http
/recommend
```

### Request

```json
{
  "query": "Best gaming phone under 35000"
}
```

### Response

```json
{
  "query": "Best gaming phone under 35000",
  "recommendation": [
    {
      "rank": 1,
      "score": 0.91,
      "name": "iQOO Neo 10",
      "price": 32000,
      "camera": "Good",
      "battery": "Excellent",
      "gaming": "Excellent",
      "processor": "Snapdragon 8 Gen 2"
    }
  ]
}
```

---

## 🏃 Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## 📈 Future Enhancements

### SmartPick AI v2

* LLM-powered recommendation generation
* OpenAI / Gemini integration
* Retrieval-Augmented Generation (RAG)
* Vector database support
* Personalized recommendations
* Web-based frontend
* Product comparison mode

---

## 🎯 Learning Outcomes

This project was built to understand the core concepts behind modern AI systems:

* Embeddings
* Semantic Search
* Similarity Ranking
* Retrieval Systems
* FastAPI APIs
* Recommendation Engines
* RAG Foundations

### Key Insight

```text
Retriever finds information.

LLM explains information.
```

Understanding this distinction is fundamental to building modern AI applications.

---

## 📜 License

MIT License
