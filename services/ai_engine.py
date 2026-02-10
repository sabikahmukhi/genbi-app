import pandas as pd
import os
from openai import OpenAI

# Create OpenAI client (API key comes from environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_insights(df: pd.DataFrame, question: str) -> str:
    """
    Generate AI insights from a pandas DataFrame
    """
    if df.empty:
        return "The dataset is empty. Please provide data."

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
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
