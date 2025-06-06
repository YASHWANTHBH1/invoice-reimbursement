def build_invoice_prompt(policy_text, invoice_text):
    return f"""
You are a reimbursement assistant. Review the HR policy and the invoice below.

HR POLICY:
{policy_text}

INVOICE:
{invoice_text}

Classify:
Status: <Fully Reimbursed | Partially Reimbursed | Declined>
Reason: <Explain why>
"""