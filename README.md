# ChopMetrics

ChopMetrics is an automated weekly insights engine built for New York’s Chopped Cheese and scalable to any small business. It ingests data from multiple sources (sales, delivery, content, reviews, and web analytics), processes it via OpenAI, and generates recap reports for both ownership and managers — fully hands-off.

---

## 🔧 Features

- Automated data ingestion from:
  - POS exports
  - Uber Eats, DoorDash, Grubhub
  - Instagram stats
  - Google & Yelp reviews
  - Wix or Shopify web analytics
- AI-generated weekly recaps via OpenAI API
- Customizable reports: Ownership vs. Store-level
- Cron-powered scheduling (no human interaction)
- Scalable to multiple brands and locations
- Postgres-ready for future analytics dashboards

---

## 🧱 Tech Stack

- **Backend**: Python, FastAPI
- **Data**: PostgreSQL, dotenv
- **AI**: OpenAI API (GPT-4o)
- **Scheduler**: Cron jobs
- **Deployment**: GitHub + Docker (optional)

---

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/chopmetrics.git
cd chopmetrics/backend

# Create virtual environment and activate
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup database
alembic upgrade head

# Run ingestion job
python cron/weekly_ingest.py