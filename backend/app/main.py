# backend/app/main.py

from fastapi import FastAPI
from app.routes import reports
import os

# This loads your .env file automatically.
from dotenv import load_dotenv

DATABASE_URL = os.getenv("DATABASE_URL")

# Create your SQLAlchemy engine
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)

load_dotenv()

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
python - dotenv
httpx
openai
psycopg2 - binary
sqlalchemy
pydantic

# .env.example

OPENAI_API_KEY = your - openai - key
DATABASE_URL = os.getenv("DATABASE_URL")
CRON_SCHEDULE = "0 9 * * MON"  # Every Monday at 9AM

# backend/cron/weekly_ingest.py


def run_weekly_ingestion():
    print("[✓] Weekly data ingestion process started...")
    # Here you'll ingest sales, delivery, content, etc.
    # Stubbed for now
    print("[✓] Data ingested and report sent.")


if __name__ == "__main__":
    run_weekly_ingestion()

# backend/README.md
