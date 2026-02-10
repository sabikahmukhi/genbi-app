import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Drop empty columns
    df = df.dropna(axis=1, how="all")

    # Try converting dates
    for col in df.columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col], errors="ignore")

    return df
