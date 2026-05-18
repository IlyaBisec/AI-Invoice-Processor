# PDF processing service.
# Extracts raw text and invoice fields from PDF files
# 18.05.2026 (c) ilya_bisec

import pdfplumber
import re


def extract_invoice_data(file_path: str):
    with pdfplumber.open(file_path) as pdf:
        text = ""

        for page in pdf.pages:
            text += page.extract_text() + "\n"

    invoice_number = re.search(r"Invoice\s*#?:?\s*(\S+)", text)
    amount = re.search(r"Total\s*:?[ ]?([$€]?\d+[.,]?\d*)", text)
    date = re.search(r"Date\s*:?[ ]?(\d{2}/\d{2}/\d{4})", text)

    return {
        "company": text.split("\n")[0][:100],
        "invoice_number": invoice_number.group(1) if invoice_number else "UNKNOWN",
        "invoice_date": date.group(1) if date else "UNKNOWN",
        "total_amount": float(
            amount.group(1)
            .replace("€", "")
            .replace("$", "")
            .replace(",", "")
        ) if amount else 0,
        "currency": "EUR",
        "raw_text": text,
    }