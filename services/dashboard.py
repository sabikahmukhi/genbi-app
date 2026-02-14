import pandas as pd
import plotly.express as px


def auto_dashboard(df: pd.DataFrame):
    charts = []

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include="object").columns.tolist()

    # Bar chart: first categorical vs first numeric
    if categorical_cols and numeric_cols:
        fig = px.bar(
            df,
            x=categorical_cols[0],
            y=numeric_cols[0],
            title=f"{numeric_cols[0]} by {categorical_cols[0]}"
        )
        charts.append(fig)

    # Histogram for numeric columns
    for col in numeric_cols[:2]:
        fig = px.histogram(df, x=col, title=f"Distribution of {col}")
        charts.append(fig)

    return charts
