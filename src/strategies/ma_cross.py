import pandas as pd
import numpy as np
import yfinance as yf
from ta.trend import EMAIndicator, SMAIndicator

# Function to calculate the moving average
def calculate_ma(data, ma_type, length):
    if ma_type == "SMA":
        return SMAIndicator(close=data, window=length).sma_indicator()
    elif ma_type == "EMA":
        return EMAIndicator(close=data, window=length).ema_indicator()
    elif ma_type == "RMA":
        return data.rolling(window=length).mean()  # Simplified RMA using rolling mean

# Load data
data = yf.download("EURUSD=X", period="1y", interval="1h")
data = data[['Close']]
data.dropna(inplace=True)

# Define MA parameters
type_ma1 = "SMA"  # Change this to RMA or EMA as needed
length_ma1 = 10
type_ma2 = "SMA"  # Change this to RMA or EMA as needed
length_ma2 = 100

# Calculate moving averages
data['MA1'] = calculate_ma(data['Close'], type_ma1, length_ma1)
data['MA2'] = calculate_ma(data['Close'], type_ma2, length_ma2)

# Generate buy and sell signals
data['buy'] = np.where(data['MA1'] > data['MA2'], 1, 0)
data['sell'] = np.where(data['MA1'] < data['MA2'], -1, 0)

# Create a signal column
data['Signal'] = data['buy'] + data['sell']

# Print the result
print(data[['Close', 'MA1', 'MA2', 'Signal']].tail(10))

# Example visualization (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='black')
plt.plot(data['MA1'], label=f'MA1 ({type_ma1} {length_ma1})', color='blue', linewidth=2)
plt.plot(data['MA2'], label=f'MA2 ({type_ma2} {length_ma2})', color='red', linewidth=2)

# Plot buy and sell signals
plt.plot(data[data['Signal'] == 1].index, data['MA1'][data['Signal'] == 1], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(data[data['Signal'] == -1].index, data['MA2'][data['Signal'] == -1], 'v', markersize=10, color='r', label='Sell Signal')

plt.title('Moving Average Cross Strategy')
plt.legend()
plt.show()
