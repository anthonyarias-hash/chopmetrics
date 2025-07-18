# backend/app/services/generate_report.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_weekly_recap(context: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a business analyst writing clear, motivating weekly recaps for a restaurant brand.",
                },
                {
                    "role": "user",
                    "content": f"Here is the data for the week:\n\n{context}\n\nPlease summarize the performance clearly and propose actionable insights.",
                },
            ],
            temperature=0.7,
            max_tokens=1200,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[!] OpenAI error: {e}")
        return "Failed to generate report"
