import os
from fastapi import APIRouter
from pydantic import BaseModel
from vectorstore.store import query_vector_db
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)
router = APIRouter()
class QueryInput(BaseModel):
    query: str
@router.post("/chatbot_query")
async def chatbot_query(input: QueryInput):
    retrieved = query_vector_db(input.query)
    docs = retrieved.get("documents", [[]])[0]
    context = "\n\n".join(docs)
    prompt = f"""
You are an assistant. Use the following invoice data to answer:
{context}
Question: {input.query}
Answer in markdown.
"""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.2
    )
    return {"answer": response.choices[0].message.content}


