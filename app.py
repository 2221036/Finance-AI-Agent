import streamlit as st
from tools import (
    load_csv,
    categorize_transactions,
    monthly_summary,
    category_analysis,
    budget_alerts,
    generate_charts,
    export_report
)

st.set_page_config(page_title="Personal Finance AI Agent")

st.title("💰 Personal Finance AI Agent")

uploaded_file = st.file_uploader("Upload Expense CSV", type=["csv"])

if uploaded_file is not None:
    df = load_csv(uploaded_file)

    st.subheader("Dataset")
    st.dataframe(df)

    df = categorize_transactions(df)

    st.subheader("Monthly Summary")
    st.write(monthly_summary(df))

    st.subheader("Category Analysis")
    st.write(category_analysis(df))

    st.subheader("Budget Alerts")
    st.write(budget_alerts(df))

    generate_charts(df)
    export_report(df)

    st.success("Charts and report generated successfully!")