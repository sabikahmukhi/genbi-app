import pandas as pd
import requests

def load_tables_from_url(url):
    
    # If it's a CSV file
    if url.endswith(".csv"):
        df = pd.read_csv(url)
        return [df]  # return list to keep structure consistent

    # Otherwise treat as HTML page
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    tables = pd.read_html(response.text)
    return tables
