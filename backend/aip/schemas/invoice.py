# API schema layer.
# Defines response/request validation models
# 18.05.2026 (c) ilya_bisec

from pydantic import BaseModel


class InvoiceResponse(BaseModel):
    id: int
    company: str
    invoice_number: str
    invoice_date: str
    total_amount: float
    currency: str
    summary: str

    class Config:
        from_attributes = True