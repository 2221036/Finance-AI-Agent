from langchain_ollama import ChatOllama

from tools import (
    load_csv,
    dataset_info,
    categorize_transactions,
    monthly_summary,
    category_analysis,
    budget_alert,
    generate_charts,
    export_report
)

# Load the LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def finance_analysis():
    try:
        # Load CSV
        df = load_csv("data/sample_expenses.csv")

        # Process data
        df = categorize_transactions(df)

        # Run all tools
        info = dataset_info(df)
        summary = monthly_summary(df)
        category = category_analysis(df)
        alerts = budget_alert(df)
        charts = generate_charts(df)
        report = export_report(df)

        result = f"""
=============================
PERSONAL FINANCE REPORT
=============================

DATASET INFO
{info}

MONTHLY SUMMARY
{summary}

CATEGORY ANALYSIS
{category}

BUDGET ALERTS
"""

        for alert in alerts:
            result += f"\n- {alert}"

        result += f"""

CHARTS
{charts}

REPORT
{report}

=============================
"""

        return result

    except Exception as e:
        return f"Error: {e}"


print("💰 Personal Finance AI Agent Started!")

while True:

    question = input("\nAsk your Finance AI Agent (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    keywords = [
        "expense",
        "expenses",
        "summary",
        "report",
        "budget",
        "analysis",
        "category",
        "chart",
        "finance"
    ]

    if any(word in question.lower() for word in keywords):
        print(finance_analysis())
    else:
        response = llm.invoke(question)
        print("\nAI:")
        print(response.content)