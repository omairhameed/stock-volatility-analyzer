import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["AAPL", "TSLA", "NVDA", "AMZN", "MSFT", "GOOGL", "META", "JPM", "BA", "NFLX"]

volatility_data = []
returns_data = []

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")

        if len(hist) < 10:
            continue

        hist["Daily Change %"] = hist["Close"].pct_change() * 100

        volatility = hist["Daily Change %"].std()

        start_price = hist["Close"].iloc[0]
        end_price = hist["Close"].iloc[-1]
        return_pct = ((end_price - start_price) / start_price) * 100

        volatility_data.append({"Ticker": ticker, "Volatility (%)": round(volatility, 2)})
        returns_data.append({"Ticker": ticker, "1-Month Return (%)": round(return_pct, 2)})

    except Exception as e:
        print(f"Error with {ticker}: {e}")

df_vol = pd.DataFrame(volatility_data).sort_values(by="Volatility (%)", ascending=False)
df_return = pd.DataFrame(returns_data).sort_values(by="1-Month Return (%)", ascending=False)

# barchart
plt.figure(figsize=(10, 6))
plt.bar(df_vol["Ticker"], df_vol["Volatility (%)"])
plt.title("Top 10 Most Volatile Stocks (Last 1 Month)")
plt.xlabel("Stock")
plt.ylabel("Volatility (%)")
plt.grid(True)
plt.tight_layout()
plt.show()


print("\n📈 1-Month Returns Leaderboard:")
print(df_return)
