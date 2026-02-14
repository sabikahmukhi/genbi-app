import streamlit as st
import pandas as pd

from services.cleaning import clean_data
from services.visualization import auto_charts
from services.ai_engine import generate_insights
#from services.ingestion import load_data_from_url\
from services.ingestion import load_tables_from_url
from services.dashboard import auto_dashboard


st.set_page_config(page_title="GenBI App", layout="wide")
st.title("🧠 Generative BI Web App")

st.subheader("📥 Data Input")

#url = st.text_input("Enter a URL (with tables)")

wiki_url = st.text_input(
    "Paste a Wikipedia URL",
    "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
)
uploaded_file = st.file_uploader("Or upload a CSV", type=["csv"])
df = None
if wiki_url:
    try:
        tables = load_tables_from_url(wiki_url)
        st.success(f"Found {len(tables)} tables")

        table_index = st.selectbox(
            "Select a table",
            range(len(tables)),
            format_func=lambda x: f"Table {x}"
        )

        df = tables[table_index]
        st.dataframe(df.head())

    except Exception as e:
        st.error(f"Failed to load tables: {e}")


elif uploaded_file:
    df = pd.read_csv(uploaded_file)



question = st.text_input(
    "Ask a question about your data",
    "Give me key insights and trends"
)


#if url:
#    df = load_data_from_url(url)

#if uploaded_file:
#    df = pd.read_csv(uploaded_file)

if df is not None:
    st.subheader("Raw Data")
    st.dataframe(df.head())

    df_clean = clean_data(df)

    st.subheader("Cleaned Data")
    st.dataframe(df_clean.head())

    st.subheader("📊 Auto Dashboard")
    auto_charts(df_clean)

   # st.subheader("📝 AI Insights")
   # st.write(generate_insights(df_clean))
    
    if st.button("Generate AI Insights"):
        with st.spinner("Thinking..."):
            insights = generate_insights(df_clean, question)
            st.subheader("AI Insights")
            st.write(insights)

