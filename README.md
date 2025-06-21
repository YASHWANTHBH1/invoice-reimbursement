
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
![Screenshot 2025-06-06 182008](https://github.com/user-attachments/assets/579270ba-fe20-411d-890b-ace3adb943c9)

2. It sends the info to a powerful AI model
   The AI reads your policy and invoices, then decides if each invoice is valid or noot.
![Screenshot 2025-06-06 182034](https://github.com/user-attachments/assets/2e37ce7e-8548-4ee5-82e5-abcd5b79d4d8)

3. It stores the results
   So you can download a summary in JSON or CSV formats.
![Screenshot 2025-06-06 191309](https://github.com/user-attachments/assets/818536fe-0d79-4bdb-be02-27f7d203ac2b)

4. You can ask questions or query it 
   Like “invoice approved?” or “What’s the policy on travel expenses?”  
   The AI uses smart search to find related info and answers you clearly.
![Screenshot 2025-06-06 191417](https://github.com/user-attachments/assets/9a3a74ad-3fe2-4320-9d5e-ad2ca3fce1cd)
![Screenshot 2025-06-06 191505](https://github.com/user-attachments/assets/f47f90e6-08fa-4c9d-90df-d4a016e76c02)
![Screenshot 2025-06-06 191538](https://github.com/user-attachments/assets/4b33c1b4-6b46-407f-b11c-cd4e2ce964c0)


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

![Screenshot 2025-06-06 194856](https://github.com/user-attachments/assets/c8b7226a-43c7-4634-b019-5c9e8f14c27d)


---

Hello,
I’ve completed the internship assessment and submitted the required files. I’m very interested in the opportunity to join your team as an intern and would love to contribute, learn, and grow together. Looking forward to hearing from you!

Best,
Yashwanth BH


Thank you


