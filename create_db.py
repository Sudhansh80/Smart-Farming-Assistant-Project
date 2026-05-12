from rag_pipeline import *

print("Loading documents...")
docs = load_documents()

print("Splitting documents...")
chunks = split_documents(docs)

print("Creating vector database...")
db = create_vector_db(chunks)

print("Vector database created successfully!")