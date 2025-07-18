# backend/app/utils/report_generator.py

import openai
import os
from app.prompts import owner_report_prompt, store_report_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_owner_report(data: dict) -> str:
    prompt = owner_report_prompt.format(input_data=data)
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']

def generate_store_report(data: dict) -> str:
    prompt = store_report_prompt.format(input_data=data)
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']