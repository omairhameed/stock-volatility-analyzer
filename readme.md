# Stock Volatility & Return Analyzer

A beginner Python tool that pulls real-time stock data and ranks the most **volatile** and **best-performing** stocks over the past month.

This was built to showcase beginner-level data science skills applied to real-world financial data.

---

# What It Does

- Retrieves price history for selected tickers using `yfinance`
- Calculates:
  - Daily price **volatility** (standard deviation of % daily change)
  - **1-month return** (percentage change from first to last closing price)
- Visualizes volatility as a bar chart
- Displays a terminal leaderboard of 1-month returns

---

# Tech Stack

- Python
- `yfinance` – pulls real market data
- `pandas` – data manipulation
- `matplotlib` – visualization



