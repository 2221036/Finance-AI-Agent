# 💰 Finance AI Agent

An AI-powered personal finance analysis application that helps users understand their expenses, analyze spending patterns, visualize financial data, and generate reports.

## 🚀 Features

- 📊 Expense data analysis
- 💰 Income and expense calculation
- 📈 Category-wise expense analysis
- 📉 Expense visualization using charts
- 🤖 AI-powered financial analysis
- 📁 Support for user CSV data
- 🚨 Budget alerts
- 📄 Expense report generation
- 📥 Export analyzed data
- 🌐 Interactive Streamlit web application

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit
- LangChain
- Ollama
- CSV Data Processing

## 📂 Project Structure

```text
Finance-AI-Agent/
│
├── app.py
├── agent.py
├── finance_app.py
├── tools.py
├── charts.py
├── report.py
├── utility.py
├── test.py
├── sample_expenses.csv
├── requirements.txt
├── README.md
└── data/


📊 What This Project Does

The Finance AI Agent analyzes financial transaction data and provides useful information about income, expenses, savings, and spending categories.
The application can categorize transactions such as:
🍔 Food
🚕 Travel
🛍️ Shopping
💡 Bills
💰 Income
📦 Others


📈 Expense Analysis

The application calculates:
Total Income
Total Expenses
Total Savings
Category-wise Expenses
Budget Status
It also creates charts to make financial information easier to understand.


📊 Visualizations

The project generates visualizations such as:
Expense Distribution Pie Chart
Category-wise Expense Bar Chart
These charts help users quickly identify where most of their money is being spent.


📁 User Data

Users can import their own financial data using a CSV file.
Example:
Date,Description,Amount
2026-01-01,Salary,50000
2026-01-03,Swiggy,-500
2026-01-05,Uber,-300
2026-01-07,Amazon,-1500
The application processes the data and provides financial analysis.


🚨 Budget Alerts

The system can compare spending against predefined budgets and notify users when spending exceeds the budget.
Example:
⚠️ Budget exceeded for Food
✅ Travel is within budget


📄 Report Generation

The application can generate an expense report containing the analyzed transaction data.
Reports can be exported as CSV files for future reference.
⚙️ Installation
Clone the repository:
git clone https://github.com/2221036/Finance-AI-Agent.git

Move into the project folder:
cd Finance-AI-Agent

Install the required packages:
pip install -r requirements.txt


▶️ Run the Application
Start the Streamlit application:
streamlit run app.py
The application will open in your browser.


🧪 Testing
The project also contains testing code.
Run:
python test.py


🎯 Project Objectives
The main objectives of this project are:
To analyze personal financial data.
To understand spending patterns.
To categorize financial transactions.
To visualize expenses.
To provide budget alerts.
To generate financial reports.
To provide an easy-to-use AI-powered finance assistant.


🔮 Future Improvements
Future versions may include:
Advanced AI financial recommendations
Monthly and yearly financial dashboards
Automatic budget planning
Expense prediction
Excel file support
Database integration
User authentication
Cloud deployment
Personalized financial recommendations


