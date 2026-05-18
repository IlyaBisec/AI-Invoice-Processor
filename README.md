# AI Invoice Processor

AI-powered invoice processing backend for automating financial document workflows.

The system allows users to upload PDF invoices and automatically extracts structured financial data using AI, stores it in a database, and provides export capabilities.

---

## Features

- Upload PDF invoices
- AI-powered data extraction:
  - invoice number
  - date
  - total amount
  - company name
- AI-generated summary of invoice content
- Store structured data in PostgreSQL
- Export data to CSV / JSON
- Search & filter invoices
- Swagger API documentation
- Dockerized deployment
- Async-ready architecture (expandable)

---

## Tech Stack

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Uvicorn

### AI & Processing
- OpenAI API
- pdfplumber / PyMuPDF

### DevOps
- Docker
- Docker Compose

---

## Project Structure

```

AI Invoice Processor/
│
├── backend/
│   ├── aip/
│   │   ├── api/         # API routes
│   │   ├── core/        # config, settings, DB, security
│   │   ├── models/      # SQLAlchemy models
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── services/    # business logic (AI, parsing)
│   │   └── utils/       # helpers
│   │
│   ├── uploads/         # uploaded PDFs
│   ├── alembic/         # migrations
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── .env
│
├── .venv/
├── README.md
└── LICENSE

````

---

## Setup & Run

### 1. Clone repository
```bash
git clone <repo-url>
cd AI Invoice Processor/backend
````

### 2. Create environment variables

Create `.env` file:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/invoices
OPENAI_API_KEY=your_key_here
```

### 3. Run with Docker

```bash
docker compose up --build
```

Backend will be available at:

```
http://localhost:8000
```

Swagger docs:

```
http://localhost:8000/docs
```

---

## API Endpoints

### Upload invoice

```
POST /invoices/upload
```

### Get invoices

```
GET /invoices
```

### Get single invoice

```
GET /invoices/{id}
```

### Export data

```
GET /invoices/export?format=csv
GET /invoices/export?format=json
```

---

## Database

Uses PostgreSQL.

Tables are managed via Alembic migrations:

```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

---

## Docker Services

* `aip_app` — FastAPI backend
* `database` — PostgreSQL

---

## Future Improvements

* Async processing (Celery + Redis)
* Multi-user authentication (JWT)
* Invoice tagging system
* Web UI dashboard (React / Next.js)
* OCR fallback for scanned PDFs
* S3 storage integration

---

## License

MIT License

---

## IlyaBisec

ilya.borisov.bisec@gmail.com
(c) 2026
