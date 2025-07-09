import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define asset tickers
assets = {
    'S&P_500': '^GSPC',       # US stock market index
    'Gold': 'GC=F',           # Gold futures
    'Crude_Oil': 'CL=F',      # Crude Oil (WTI)
    'US_Treasury_ETF': 'TLT'  # US Treasury bond ETF
}

# Date range for your study
start_date = '2025-02-01'
end_date = '2025-04-30'

# Download adjusted close prices
full_data = yf.download(list(assets.values()), start=start_date, end=end_date)

# Extract just the 'Close' prices
data = full_data['Close']

# Rename columns with friendly names
data.columns = list(assets.keys())

# Drop any missing data
data = data.dropna()

# Calculate daily log returns
returns = np.log(data / data.shift(1)).dropna()

# Print first rows to check
print("📈 Aligned Daily Log Returns:")
print(returns.head())

# Plot the prices
data.plot(title='Asset Prices (Feb–Apr 2025)', figsize=(10, 5))
plt.grid()
plt.show()

# Plot the log returns
returns.plot(title='Daily Log Returns (Feb–Apr 2025)', figsize=(10, 5))
plt.grid()
plt.show()

# Save the returns to a CSV on the Desktop
print("💾 Saving the CSV file now...")

print("💾 Saving the CSV file to C:/PythonData...")
# Save prices
print("💾 Saving asset prices to C:/PythonData...")
data.to_csv('C:/PythonData/traditional_assets_prices.csv')

# Save log returns
print("💾 Saving log returns to C:/PythonData...")
returns.to_csv('C:/PythonData/traditional_assets_log_returns.csv')
print("✅ Both prices and returns saved to C:/PythonData")
