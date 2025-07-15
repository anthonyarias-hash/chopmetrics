import json
import os
import sys
from pathlib import Path
from datetime import datetime
from app.database import SessionLocal
from app.models import SalesData, Review
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 
def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def ingest_sales_data():
    print("🧾 Ingesting sales data...")
    sales_file = Path("data/sales_sample.json")
    if sales_file.exists():
        with sales_file.open() as f:
            sales = json.load(f)
            print(f"[✓] Loaded {len(sales)} sales records")
    else:
        print("[!] Sales data file not found")

def ingest_reviews():
    print("📝 Ingesting reviews...")
    reviews_file = Path("data/reviews_sample.json")
    if reviews_file.exists():
        with reviews_file.open() as f:
            reviews = json.load(f)
            print(f"[✓] Loaded {len(reviews)} reviews")
    else:
        print("[!] Reviews file not found")
        
        

def run_weekly_ingestion():
    print("🚀 Starting weekly ingestion...")
    ingest_sales_data()
    ingest_reviews()
    print("✅ Ingestion complete")

if __name__ == "__main__":
    run_weekly_ingestion()
    
def ingest_sales(sales_path):
    print("🧾 Ingesting sales data...")
    sales_data = load_json(sales_path)
    db = SessionLocal()

    for record in sales_data:
        sale = SalesData(
            store_id=1,  # update if dynamic later
            date=datetime.strptime(record["date"], "%Y-%m-%d").date(),
            product_name=record["product_name"],
            quantity_sold=int(record["quantity_sold"]),
            total_sales=float(record["total_sales"]),
            delivery_platform=record.get("delivery_platform", "Direct"),
            source_file=sales_path
        )
        db.add(sale)

    db.commit()
    db.close()
    print("✅ Sales data ingested.")
    
def ingest_reviews(reviews_path):
    print("📝 Ingesting reviews...")
    reviews_data = load_json(reviews_path)
    db = SessionLocal()

    for record in reviews_data:
        review = Review(
            store_id=1,
            review_date=datetime.strptime(record["review_date"], "%Y-%m-%d").date(),
            platform=record["platform"],
            rating=float(record["rating"]),
            comment=record["comment"]
        )
        db.add(review)

    db.commit()
    db.close()
    print("✅ Reviews ingested.")
    
if __name__ == "__main__":
    sales_path = os.path.join("data", "sales_sample.json")
    reviews_path = os.path.join("data", "reviews_sample.json")

    ingest_sales(sales_path)
    ingest_reviews(reviews_path)
