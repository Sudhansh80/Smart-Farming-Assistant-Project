# 🌾 Smart Farming Assistant AI

## RAG-Based Agriculture Support System using Generative AI

---

# 📌 Overview

Smart Farming Assistant AI is a Retrieval-Augmented Generation (RAG) based Generative AI project developed to assist farmers and agriculture learners with intelligent farming-related answers.

The system uses:

- NLP preprocessing
- Semantic search
- Embeddings
- Vector databases
- Large Language Models (LLMs)

Users can ask agriculture-related questions, and the system retrieves relevant information from farming documents before generating AI-powered answers.

---

# 🚀 Features

- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Semantic Search using Embeddings
- ✅ Agriculture Knowledge Base
- ✅ Vector Database using ChromaDB
- ✅ AI-Powered Responses using Groq Llama 3.1
- ✅ Gradio-based User Interface
- ✅ Prompt Engineering
- ✅ Fast Document Retrieval

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Gradio | Frontend Interface |
| LangChain | RAG Pipeline |
| ChromaDB | Vector Database |
| Sentence Transformers | Embedding Generation |
| Groq API | Large Language Model |
| HuggingFace Embeddings | Semantic Embeddings |

---

# 📂 Project Structure

```text
project/
│
├── app.py
├── create_db.py
├── requirements.txt
│
├── data/
│   ├── wheat.txt
│   ├── irrigation.txt
│   ├── disease.txt
│   └── govt_scheme.txt
│
├── vector_db/
│
└── utils/
    ├── preprocess.py
    ├── embedding.py
    ├── rag_pipeline.py
    └── prompting.py
```

---

# 📚 Dataset

The project uses agriculture-related text documents as the knowledge base.

## Topics Covered

- Wheat farming
- Irrigation methods
- Crop diseases
- Government schemes
- Fertilizer usage
- Water conservation

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## 2️⃣ Open Project Folder

```bash
cd project
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv project
```

---

## 4️⃣ Activate Environment

### Windows

```bash
project\Scripts\activate
```

### Linux / Mac

```bash
source project/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

## Create Vector Database

```bash
python create_db.py
```

---

## Start Application

```bash
python app.py
```

---

# 🌐 Open in Browser

```text
http://127.0.0.1:7860
```

---

# 💬 Example Queries

- What is drip irrigation?
- How to improve wheat production?
- What is PM-Kisan scheme?
- How can farmers prevent crop diseases?
- Which irrigation method saves water?

---

# 🧠 How RAG Works

```text
User Query
↓
Embedding Generation
↓
Vector Database Search
↓
Semantic Retrieval
↓
Prompt Engineering
↓
LLM Response Generation
↓
Final AI Answer
```

---

# 🔍 Embeddings & Semantic Search

The project uses:

```text
all-MiniLM-L6-v2
```

to generate embeddings for semantic similarity search.

Cosine similarity is used for retrieving relevant document chunks.

---

# 🤖 Large Language Model

The project uses:

```text
llama-3.1-8b-instant
```

through the Groq API for fast AI response generation.

---

# ⚠️ Ethical Considerations

## Bias
The AI model may provide incomplete farming advice.

## Privacy
User data is not stored.

## Misuse
Users should consult agriculture experts before applying recommendations.

---

# 📸 Screenshots

Add:
- Application UI screenshots
- Retrieval examples
- AI response examples
- Code screenshots

---

# 📌 Future Improvements

- Voice-based farming assistant
- Hindi/Punjabi language support
- Weather API integration
- Image-based crop disease detection
- Mobile app version

---

# 👨‍💻 Developed By

## Sudhansh Ranta
### Roll No: 66
### Registration No: 12411099

---

# 📄 License

This project is developed for academic and educational purposes.
