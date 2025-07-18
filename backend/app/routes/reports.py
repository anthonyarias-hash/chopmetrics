# backend/app/routes/reports.py

from fastapi import APIRouter
from app.utils.report_generator import generate_owner_report, generate_store_report
import json

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/generate")
def generate_report():
    # Load sample input from file for now
    with open("backend/data/sales_sample.json") as f:
        sales_data = json.load(f)
    with open("backend/data/reviews_sample.json") as f:
        reviews_data = json.load(f)

    combined_data = {
        "sales": sales_data,
        "reviews": reviews_data,
        # Add more fields later: marketing, delivery, etc.
    }

    owner_report = generate_owner_report(combined_data)
    store_report = generate_store_report(combined_data)

    return {
        "status": "success",
        "owner_report": owner_report,
        "store_report": store_report
    }
