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

## 🚀 Quickstart (Dev)

```bash
cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
