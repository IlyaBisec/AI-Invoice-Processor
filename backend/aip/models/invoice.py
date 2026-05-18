# ORM model layer.
# Defines Invoice database table schema
# 18.05.2026 (c) ilya_bisec

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime

from aip.core.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    invoice_number = Column(String)
    invoice_date = Column(String)
    total_amount = Column(Float)
    currency = Column(String)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)