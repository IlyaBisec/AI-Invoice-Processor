# Business logic layer.
# Handles database operations for invoices
# 18.05.2026 (c) ilya_bisec

from sqlalchemy.orm import Session

from aip.models.invoice import Invoice


def create_invoice(db: Session, data: dict):
    invoice = Invoice(
        company=data["company"],
        invoice_number=data["invoice_number"],
        invoice_date=data["invoice_date"],
        total_amount=data["total_amount"],
        currency=data["currency"],
        summary=data["summary"],
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice