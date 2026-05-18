# Export utility layer.
# Handles exporting invoices to CSV format
# 18.05.2026 (c) ilya_bisec

import pandas as pd


def export_to_csv(invoices, file_name="invoices.csv"):
    data = []

    for invoice in invoices:
        data.append({
            "company": invoice.company,
            "invoice_number": invoice.invoice_number,
            "invoice_date": invoice.invoice_date,
            "amount": invoice.total_amount,
            "currency": invoice.currency,
        })

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)

    return file_name