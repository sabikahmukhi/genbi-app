import plotly.express as px
import streamlit as st
import pandas as pd

def auto_charts(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(exclude="number").columns

    if len(numeric_cols) > 0 and len(categorical_cols) > 0:
        fig = px.bar(
            df,
            x=categorical_cols[0],
            y=numeric_cols[0],
            title=f"{numeric_cols[0]} by {categorical_cols[0]}"
        )
        st.plotly_chart(fig, use_container_width=True)
