# Application entrypoint.
# Initializes FastAPI app and routes
# 18.05.2026 (c) ilya_bisec

from fastapi import FastAPI

from aip.api.routes.invoices import router as invoice_router
from aip.core.database import Base, engine

#Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Invoice Processor",
    version="1.0.0"
)

app.include_router(invoice_router)


@app.get("/")
def root():
    return {
        "message": "AI Invoice Processor API"
    }