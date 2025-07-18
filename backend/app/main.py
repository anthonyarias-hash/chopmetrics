# backend/app/main.py
from fastapi import APIRouter
from fastapi import FastAPI
from app.routes import reports
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
app = FastAPI(title="ChopMetrics API")
app.include_router(reports.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to ChopMetrics"}





router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/generate")
def generate_report():
    return {"status": "success", "message": "Weekly report generated (stub)"}



# backend/cron/weekly_ingest.py


def run_weekly_ingestion():
    print("[✓] Weekly data ingestion process started...")
    # Here you'll ingest sales, delivery, content, etc.
    # Stubbed for now
    print("[✓] Data ingested and report sent.")


if __name__ == "__main__":
    run_weekly_ingestion()

# backend/README.md
