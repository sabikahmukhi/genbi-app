import pandas as pd

def load_data_from_url(url: str):
    """
    Tries to extract tables from a webpage.
    Returns the first table found.
    """
    try:
        tables = pd.read_html(url)
        if len(tables) == 0:
            return None
        return tables[0]
    except Exception as e:
        return None
