import streamlit as st
import requests
import json

# ✅ Streamlit page setup
st.set_page_config(page_title="Invoice Reimbursement UI", layout="centered")
st.title("💸 Invoice Reimbursement Portal")

# ✅ API base URL
API_BASE = "http://localhost:8000"

# ✅ Sidebar navigation
page = st.sidebar.radio("Choose", ["Analyze Invoices", "Chatbot Query"])
st.success("✅ App loaded")
st.write("Selected page:", page)

# ✅ Analyze Invoices Section
if page == "Analyze Invoices":
    st.header("📤 Upload HR Policy & Invoices")

    policy_pdf = st.file_uploader("Upload Policy PDF", type=["pdf"])
    invoices_zip = st.file_uploader("Upload Invoices ZIP", type=["zip"])
    emp_name = st.text_input("Employee Name")

    if st.button("Analyze"):
        if not (policy_pdf and invoices_zip and emp_name):
            st.warning("⚠️ Please upload both files and enter employee name.")
        else:
            st.info("📨 Submitting to API... Please wait.")
            try:
                files = {
                    "policy_pdf": (policy_pdf.name, policy_pdf, "application/pdf"),
                    "invoices_zip": (invoices_zip.name, invoices_zip, "application/zip")
                }
                data = {"employee_name": emp_name}
                response = requests.post(f"{API_BASE}/analyze_invoices", files=files, data=data)

                if response.status_code == 200:
                    st.success("✅ Analysis Complete")
                    results = response.json().get("results", [])
                    for res in results:
                        st.markdown(f"**📄 Invoice:** {res['invoice']}")
                        st.markdown(f"**✅ Status:** {res['status']}")
                        st.markdown(f"**📝 Reason:** {res['reason']}")

                    # ✅ Download JSON button
                    download_json = requests.get(f"{API_BASE}/download_results/{emp_name}?format=json")
                    if download_json.status_code == 200:
                        st.download_button(
                            label="📥 Download Results (JSON)",
                            data=download_json.content,
                            file_name=f"{emp_name}_results.json",
                            mime="application/json"
                        )

                    # ✅ Download CSV button
                    download_csv = requests.get(f"{API_BASE}/download_results/{emp_name}?format=csv")
                    if download_csv.status_code == 200:
                        st.download_button(
                            label="📥 Download Results (CSV)",
                            data=download_csv.content,
                            file_name=f"{emp_name}_results.csv",
                            mime="text/csv"
                        )
                else:
                    st.error(f"❌ API returned status {response.status_code}")
                    try:
                        st.json(response.json())
                    except Exception:
                        st.text("⚠️ Could not parse JSON response:")
                        st.text(response.text)
            except Exception as e:
                st.error(f"⚠️ Exception occurred: {e}")

# ✅ Chatbot Query Section
elif page == "Chatbot Query":
    st.header("💬 Ask Questions")
    query = st.text_input("Type a question like: 'What invoices were declined for Hardik?'")

    if st.button("Ask") and query:
        st.info("🤖 Sending query to chatbot...")
        try:
            res = requests.post(f"{API_BASE}/chatbot_query", json={"query": query})
            if res.status_code == 200:
                st.markdown("### 🧠 Answer")
                st.markdown(res.json()["answer"], unsafe_allow_html=True)
            else:
                st.error(f"❌ Chatbot API error: {res.status_code}")
                try:
                    st.json(res.json())
                except Exception:
                    st.text("⚠️ Could not parse JSON response:")
                    st.text(res.text)
        except Exception as e:
            st.error(f"⚠️ Exception occurred: {e}")



