from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def load_documents():

    docs = []

    files = [
        "data/wheat.txt",
        "data/irrigation.txt",
        "data/disease.txt",
        "data/govt_scheme.txt"
    ]

    for file in files:
        loader = TextLoader(file)
        docs.extend(loader.load())

    return docs

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )

    return splitter.split_documents(documents)

def create_vector_db(chunks):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="vector_db"
    )

    vectordb.persist()

    return vectordb