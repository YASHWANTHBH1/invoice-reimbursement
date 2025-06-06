assignment
# Invoice Reimbursement System

This project is a simple web app built with Python’s FastAPI. It helps companies analyze their invoices and answer questions about them using advanced AI models.

You can:

- Upload your company’s policy document and a bunch of invoices in one go.
- The app reads everything, checks which invoices follow the rules, and tells you if they can be reimbursed.
- Ask questions in natural language about your invoices or policies and get smart answers from the AI.

---

how it work?

1. upload a policy PDF and a ZIP file with invoice  
   The app extracts the text from these files.

2. It sends the info to a powerful AI model
   The AI reads your policy and invoices, then decides if each invoice is valid or noot.

3. It stores the results
   So you can download a summary in JSON or CSV formats.

4. You can ask questions or query it 
   Like “invoice approved?” or “What’s the policy on travel expenses?”  
   The AI uses smart search to find related info and answers you clearly.

---

What technologies are used?

- FastAPI: The web framework that runs the app.  
- Groq API: Provides the AI model (LLaMA 3) for understanding and answering.  
- Sentence Transformers & ChromaDB: Convert text to vectors and find similar documents quickly.  
- Python tools:To read PDFs, handle files, and organize everything.
  So this project is like an invoice checking system. We used bunch of python tools to make it work easy. Like os is used to create folders and manage paths, and shutil help us unzip invoice files which user upload. Then we used uuid to give each invoice a unique name so it not clash. To store results we used json and csv because some people like Excel and some like raw data. If something crash, traceback shows us error, so we know what went wrong.
   For the website part, we used FastAPI — it's fast and good for APIs. Then we used pydantic so we can check if people gave us proper data when they call our API. We keep our API key safe in .env file and used dotenv to read that. So no need to hardcode secret things.
   To make the chatbot smart, we used sentence-transformer to convert text to some math form . Then with chromadb we store those vectors and when user ask something, we can find similar documents quickly. And finally the hero is openai but we use it with Groq API and it talks to the LLaMA3 model. It gives nice answers like “This invoice exceeds the limit” and explains why.

---

How to setup

1. Clone the project to your computer.

2. Install the necessary Python packages:
 ex : pip install -r requirements.txt
3. Create a file named .env in the project dir and add your Groq API key in to it :
 ex :GROQ_API_KEY=your_actual_api_key_here
4. Run the app server api with:
 ex : uvicorn main:app --reload
5. run streamlit using the terminal:
 ex :go the ui folder and in cmd run = streamlit run app.py

---

file structure :


---

Hello,
I’ve completed the internship assessment and submitted the required files. I’m very interested in the opportunity to join your team as an intern and would love to contribute, learn, and grow together. Looking forward to hearing from you!

Best,
Yashwanth BH


Thank you


