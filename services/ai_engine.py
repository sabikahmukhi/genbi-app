import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not found. Check your .env file.")
    return OpenAI(api_key=api_key)


def generate_insights(df: pd.DataFrame, question: str) -> str:
    client = get_client()

    sample_data = df.head(10).to_csv(index=False)

    prompt = f"""
You are a business data analyst.

Here is sample data:
{sample_data}

User question:
{question}

Give clear, concise, business-friendly insights.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
