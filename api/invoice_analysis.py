import os
import uuid
import shutil
import traceback
import json
import csv
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Query
from fastapi.responses import FileResponse
from utils.pdf_parser import extract_text_from_pdf
from utils.prompt_templates import build_invoice_prompt
from vectorstore.store import store_to_vector_db
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)
router = APIRouter()
@router.post("/analyze_invoices")
async def analyze_invoices(
    policy_pdf: UploadFile = File(...),
    invoices_zip: UploadFile = File(...),
    employee_name: str = Form(...)
):
    try:
        os.makedirs("temp/invoices", exist_ok=True)
        policy_path = "temp/policy.pdf"
        zip_path = "temp/invoices.zip"
        with open(policy_path, "wb") as f:
            f.write(await policy_pdf.read())
        with open(zip_path, "wb") as f:
            f.write(await invoices_zip.read())
        shutil.unpack_archive(zip_path, "temp/invoices")
        policy_text = extract_text_from_pdf(policy_path)
        results = []
        invoice_dir = Path("temp/invoices")
        pdf_files = list(invoice_dir.rglob("*.pdf"))

        if not pdf_files:
            return {"success": False, "error": "No PDF files found in the uploaded ZIP."}
        for file_path in pdf_files:
            try:
                invoice_text = extract_text_from_pdf(str(file_path))
                prompt = build_invoice_prompt(policy_text, invoice_text)
                print(f"\n📝 Prompt for {file_path.name}:\n", prompt[:1000])
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[{"role": "system", "content": prompt}],
                    temperature=0.3
                )
                output = response.choices[0].message.content
                print(f"📨 Response for {file_path.name}:\n", output)
                status = output.split("Status:")[1].split("\n")[0].strip()
                reason = output.split("Reason:")[1].strip()
                doc_id = f"{employee_name}-{uuid.uuid4()}"
                metadata = {"employee": employee_name, "invoice": file_path.name, "status": status}
                content = invoice_text + "\n" + reason
                store_to_vector_db(doc_id, content, metadata)
                results.append({
                    "invoice": file_path.name,
                    "status": status,
                    "reason": reason
                })
            except Exception as e:
                print(f"Error in {file_path.name}: {e}")
                results.append({
                    "invoice": file_path.name,
                    "status": "Failed",
                    "reason": f"Error analyzing this invoice: {str(e)}"
                })
        os.makedirs("downloads", exist_ok=True)
        json_path = f"downloads/{employee_name}_results.json"
        csv_path = f"downloads/{employee_name}_results.csv"

        with open(json_path, "w") as jf:
            json.dump(results, jf, indent=4)

        with open(csv_path, "w", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=["invoice", "status", "reason"])
            writer.writeheader()
            writer.writerows(results)
        shutil.rmtree("temp")
        return {"success": True, "results": results}
    except Exception as e:
        traceback.print_exc()
        return {
            "success": False,
            "error": f"Internal Server Error: {str(e)}"
        }
@router.get("/download_results/{employee_name}")
async def download_results(employee_name: str, filetype: str = Query("json")):
    filetype = filetype.lower()
    if filetype not in ("json", "csv"):
        raise HTTPException(status_code=400, detail="filetype must be 'json' or 'csv'")
    filepath = f"downloads/{employee_name}_results.{filetype}"
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")
    media_type = "application/json" if filetype == "json" else "text/csv"
    return FileResponse(filepath, media_type=media_type, filename=os.path.basename(filepath))



