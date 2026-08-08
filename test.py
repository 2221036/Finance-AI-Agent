from tools import load_csv, dataset_info, categorize_transactions, monthly_summary

df = load_csv("data/sample_expenses.csv")

print("=== Dataset ===")
print(df)

print("\n=== Dataset Information ===")
info = dataset_info(df)

for key, value in info.items():
    print(f"{key}: {value}")

print("\n=== Categorized Transactions ===")
df = categorize_transactions(df)
print(df)

print("\n=== Monthly Summary ===")
summary = monthly_summary(df)

for key, value in summary.items():
    print(f"{key}: ₹{value}")
    
from tools import load_csv, dataset_info, categorize_transactions, monthly_summary, category_analysis
    
print("\n=== Category Analysis ===")

analysis = category_analysis(df)

for key, value in analysis.items():
    print(f"{key}: ₹{value}")
    
from tools import load_csv, dataset_info, categorize_transactions, monthly_summary, category_analysis, budget_alert

print("\n=== Budget Alerts ===")

budgets = {
    "Food": 700,
    "Travel": 500,
    "Shopping": 1000,
    "Bills": 2000
}

alerts = budget_alert(df, budgets)

for alert in alerts:
    print(alert)
    
from tools import load_csv, dataset_info, categorize_transactions, monthly_summary, category_analysis, budget_alert

print("\n=== Budget Alerts ===")

budgets = {
    "Food": 700,
    "Travel": 500,
    "Shopping": 1000,
    "Bills": 2000
}

alerts = budget_alert(df, budgets)

for alert in alerts:
    print(alert)
    
from tools import load_csv, dataset_info, categorize_transactions, monthly_summary, category_analysis, budget_alert

print("\n=== Budget Alerts ===")

budgets = {
    "Food": 700,
    "Travel": 500,
    "Shopping": 1000,
    "Bills": 2000
}

alerts = budget_alert(df, budgets)

for alert in alerts:
    print(alert)
    
from tools import load_csv, dataset_info, categorize_transactions, monthly_summary, category_analysis, budget_alert, generate_charts

print("\n=== Generate Charts ===")
message = generate_charts(df)
print(message)

from tools import load_csv, dataset_info, categorize_transactions, monthly_summary, category_analysis, budget_alert, generate_charts, export_report

print("\n=== Export Report ===")
message = export_report(df)
print(message)