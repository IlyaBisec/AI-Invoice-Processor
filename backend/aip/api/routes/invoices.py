# API routes layer.
# Handles HTTP endpoints for invoice operations
# 18.05.2026 (c) ilya_bisec

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

import os
import shutil

from aip.core.database import SessionLocal
from aip.models.invoice import Invoice
from aip.services.pdf_parser import extract_invoice_data
from aip.services.ai_summary import generate_summary
from aip.services.invoice_service import create_invoice
from aip.utils.exporter import export_to_csv

router = APIRouter(prefix="/invoices", tags=["Invoices"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/upload")
def upload_invoice(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    invoice_data = extract_invoice_data(file_path)

    summary = generate_summary(invoice_data["raw_text"])

    invoice_data["summary"] = summary

    invoice = create_invoice(db, invoice_data)

    return {
        "status": "success",
        "invoice_id": invoice.id,
        "summary": summary,
    }


@router.get("/")
def get_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice).all()


@router.get("/{invoice_id}")
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()


@router.get("/export/csv")
def export_csv(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    file_name = export_to_csv(invoices)

    return FileResponse(file_name)


@router.delete("/{invoice_id}")
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()

    if not invoice:
        return {"error": "Invoice not found"}

    db.delete(invoice)
    db.commit()

    return {"status": "deleted"}