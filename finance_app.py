import streamlit as st
from tools import generate_charts
from tools import export_report
from tools import (
    load_csv,
    dataset_info,
    categorize_transactions,
    monthly_summary,
    category_analysis
)

st.set_page_config(page_title="Finance AI Agent")

st.title("💰 Finance AI Agent")

df = load_csv("sample_expenses.csv")

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Dataset Information")
st.write(dataset_info(df))

df = categorize_transactions(df)

st.subheader("Monthly Summary")
st.write(monthly_summary(df))

st.subheader("Category Analysis")
st.write(category_analysis(df))

st.subheader("Charts")
st.write(generate_charts(df))


st.subheader("Export Reports")
if st.button(export_report(df)):
    st.write(export_report(df))
    
st.subheader("Charts")

generate_charts(df)

st.image("reports/pie_chart.png")
st.image("reports/bar_chart.png")


st.subheader("Export Reports")

if st.button("Export CSV Reports"):
    st.success(export_report(df))
    
    
import streamlit as st
from tools import (
    load_csv,
    dataset_info,
    categorize_transactions,
    monthly_summary,
    category_analysis,
    generate_charts,
    export_report
)

st.set_page_config(page_title="Finance AI Agent", layout="wide")

st.title("💰 Finance AI Agent")
st.write("Upload your own expense CSV file to analyze it.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = load_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Dataset")
    st.dataframe(df)

    st.subheader("Dataset Information")
    st.write(dataset_info(df))

    df = categorize_transactions(df)

    st.subheader("Monthly Summary")
    st.write(monthly_summary(df))

    st.subheader("Category Analysis")
    st.write(category_analysis(df))

    st.subheader("Expense Charts")

    generate_charts(df)

    st.image("reports/pie_chart.png", caption="Pie Chart")
    st.image("reports/bar_chart.png", caption="Bar Chart")

    st.subheader("Export Report")

    if st.button("Export CSV Report"):
        result = export_report(df)
        st.success(result)

else:
    st.info("Please upload a CSV file to begin.")


