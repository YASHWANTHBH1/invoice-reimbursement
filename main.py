print("main.py is running")
from api import invoice_analysis, chatbot_query
print("Imported invoice_analysis and chatbot_query successfully")
from fastapi import FastAPI

app = FastAPI(
    title="Invoice Reimbursement System",
    description="LLM-based invoice analysis and chatbot",
    version="1.0"
)

# Include both API routers
app.include_router(invoice_analysis.router)
app.include_router(chatbot_query.router)
