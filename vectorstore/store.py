from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("invoices")

def store_to_vector_db(doc_id, content, metadata):
    embedding = model.encode([content])[0].tolist()
    collection.add(documents=[content], metadatas=[metadata], ids=[doc_id], embeddings=[embedding])

def query_vector_db(query):
    embedding = model.encode([query])[0].tolist()
    result = collection.query(query_embeddings=[embedding], n_results=3)
    return result
