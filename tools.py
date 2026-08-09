import pandas as pd
import matplotlib.pyplot as plt
import os


# -----------------------------
# Tool 1 - Load CSV
# -----------------------------
def load_csv(file):
    try:
        return pd.read_csv(file)
    except Exception as e:
        raise Exception(f"Error loading CSV: {e}")


# -----------------------------
# Tool 2 - Dataset Information
# -----------------------------
def dataset_info(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Column Names": list(df.columns),
        "Missing Values": df.isnull().sum().to_dict()
    }


# -----------------------------
# Tool 3 - Categorize Transactions
# -----------------------------
def categorize_transactions(df):

    categories = {
        "Swiggy": "Food",
        "Zomato": "Food",
        "Uber": "Travel",
        "Ola": "Travel",
        "Amazon": "Shopping",
        "Flipkart": "Shopping",
        "Electricity Bill": "Bills",
        "Salary": "Income"
    }

df.columns = df.columns.str.strip()
df["Description"] = df["Description"].astype(str).str.strip()
df["Category"] = df["Description"].map(categories).fillna("Others")

    return df


# -----------------------------
# Tool 4 - Monthly Summary
# -----------------------------
def monthly_summary(df):

    income = df[df["Amount"] > 0]["Amount"].sum()
    expenses = abs(df[df["Amount"] < 0]["Amount"].sum())
    savings = income - expenses

    return {
        "Total Income": income,
        "Total Expenses": expenses,
        "Total Savings": savings
    }


# -----------------------------
# Tool 5 - Category Analysis
# -----------------------------
def category_analysis(df):

    expenses = df[df["Amount"] < 0]

    category_total = (
        expenses.groupby("Category")["Amount"]
        .sum()
        .abs()
        .to_dict()
    )

    return category_total


# -----------------------------
# Tool 6 - Budget Alerts
# -----------------------------
def budget_alert(df):

    budgets = {
        "Food": 5000,
        "Travel": 3000,
        "Shopping": 4000,
        "Bills": 2000,
        "Others": 3000
    }

    expenses = df[df["Amount"] < 0]

    spending = expenses.groupby("Category")["Amount"].sum().abs()

    alerts = []

    for category, budget in budgets.items():

        spent = spending.get(category, 0)

        if spent > budget:
            alerts.append(
                f"⚠ Budget exceeded for {category}. Budget = ₹{budget}, Spent = ₹{spent}"
            )
        else:
            alerts.append(
                f"✅ {category} is within budget. Budget = ₹{budget}, Spent = ₹{spent}"
            )

    return alerts


# -----------------------------
# Tool 7 - Generate Charts
# -----------------------------
def generate_charts(df):

    os.makedirs("reports", exist_ok=True)

    expenses = df[df["Amount"] < 0]

    category_total = expenses.groupby("Category")["Amount"].sum().abs()

    plt.figure(figsize=(6,6))
    plt.pie(
        category_total,
        labels=category_total.index,
        autopct="%1.1f%%"
    )
    plt.title("Expense Distribution")
    plt.savefig("reports/pie_chart.png")
    plt.close()

    plt.figure(figsize=(6,4))
    plt.bar(category_total.index, category_total.values)
    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("reports/bar_chart.png")
    plt.close()

    return "Charts generated successfully."


# -----------------------------
# Tool 8 - Export Report
# -----------------------------
def export_report(df):

    os.makedirs("reports", exist_ok=True)

    output = "reports/expense_report.csv"

    df.to_csv(output, index=False)

    return f"Report exported to {output}"    
