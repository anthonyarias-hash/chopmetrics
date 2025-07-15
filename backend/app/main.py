# backend/app/main.py

from fastapi import FastAPI
from app.routes import reports

app = FastAPI(title="ChopMetrics API")

app.include_router(reports.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ChopMetrics"}

# backend/app/routes/reports.py

from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/generate")
def generate_report():
    return {"status": "success", "message": "Weekly report generated (stub)"}

# backend/requirements.txt

fastapi
uvicorn
python-dotenv
httpx
openai
psycopg2-binary
sqlalchemy
pydantic

# .env.example

OPENAI_API_KEY=your-openai-key
DATABASE_URL=postgresql://user:password@localhost:5432/chopmetrics
CRON_SCHEDULE="0 9 * * MON"  # Every Monday at 9AM

# backend/cron/weekly_ingest.py

import os
import dotenv

dotenv.load_dotenv()

def run_weekly_ingestion():
    print("[✓] Weekly data ingestion process started...")
    # Here you'll ingest sales, delivery, content, etc.
    # Stubbed for now
    print("[✓] Data ingested and report sent.")

if __name__ == "__main__":
    run_weekly_ingestion()

# backend/README.md

# ChopMetrics

ChopMetrics is a fully automated performance insight engine for New York's Chopped Cheese and future small businesses.

## Features
- Automated data ingestion from sales, delivery, review, and web/email sources
- Weekly recap report generation using OpenAI
- Separate emails for ownership and managers
- Admin dashboard with preview and logs

## Tech Stack
- Python (FastAPI)
- PostgreSQL
- OpenAI API
- Cron-based automation

## Quickstart

```bash
cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Cron Ingestion
To test the cron ingestion manually:

```bash
python cron/weekly_ingest.py
```

## Setup .env

```bash
cp .env.example .env
```
Update the variables with your real API keys and database connection.
