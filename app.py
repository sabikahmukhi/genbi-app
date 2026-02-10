import streamlit as st
import pandas as pd

from services.cleaning import clean_data
from services.visualization import auto_charts
from services.ai_engine import generate_insights
from services.ingestion import load_data_from_url

st.set_page_config(page_title="GenBI App", layout="wide")
st.title("🧠 Generative BI Web App")

st.subheader("📥 Data Input")

#url = st.text_input("Enter a URL (with tables)")


url = st.text_input("Enter a CSV URL")
uploaded_file = st.file_uploader("Or upload a CSV", type=["csv"])
df = None

if url:
    try:
        df = pd.read_csv(url)
        st.success("Data loaded from URL")
    except Exception as e:
        st.error(f"Failed to load URL: {e}")


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

