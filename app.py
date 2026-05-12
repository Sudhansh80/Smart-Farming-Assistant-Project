import gradio as gr
from groq import Groq

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# --------------------------------
# GROQ API KEY
# --------------------------------
client = Groq(
    api_key="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"
)

# --------------------------------
# EMBEDDING MODEL
# --------------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --------------------------------
# LOAD VECTOR DATABASE
# --------------------------------
vectordb = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

# --------------------------------
# MAIN FUNCTION
# --------------------------------
def farming_assistant(query):

    try:

        # Retrieve relevant documents
        docs = vectordb.similarity_search(query, k=2)

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        # Prompt
        prompt = f"""
You are a smart farming assistant.

Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer in simple language.
"""

        # Generate answer using Groq
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        answer = response.choices[0].message.content

        return answer

    except Exception as e:
        return f"ERROR: {str(e)}"

# --------------------------------
# GRADIO UI
# --------------------------------
interface = gr.Interface(
    fn=farming_assistant,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask farming question..."
    ),
    outputs="text",
    title="🌾 Smart Farming Assistant",
    description="RAG-based agriculture assistant using Groq + LangChain"
)

# Launch App
interface.launch()