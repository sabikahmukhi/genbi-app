import pandas as pd


def load_tables_from_url(url: str):
    """
    Loads all HTML tables from a public webpage (e.g. Wikipedia)
    """
    tables = pd.read_html(url)
    return tables
