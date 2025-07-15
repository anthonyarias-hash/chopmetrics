# backend/cron/weekly_ingest.py

import os
from dotenv import load_dotenv
from app.services.generate_report import generate_weekly_recap

load_dotenv()

def run_weekly_ingestion():
    print("[?] Weekly data ingestion process started...")

    # Replace this stub with actual compiled data
    context = """
    Hollywood: $36,572.36 in sales, 817 orders, 413 new customers
    Mid City: $14,053.13 in sales, 321 orders, 207 new customers
    Instagram: 20K followers, 11.4K reel views (Waffles), 2.1K (Plate), 4.2K (Fries)
    BOGO: Hollywood $8,082.49 | Mid City $2,847.18
    Notable: Becca D and Kelly C positive Yelp reviews, mixed Mid City Google reviews
    """

    report = generate_weekly_recap(context)

    print("[?] Recap Generated:")
    print(report)

if __name__ == "__main__":
    run_weekly_ingestion()
