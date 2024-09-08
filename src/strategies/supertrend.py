import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ta.volatility import AverageTrueRange

# Download data from Yahoo Finance
data = yf.download("EURUSD=X", period="5d", interval="1h")
data.index = pd.to_datetime(data.index)
data = data.drop(columns=['Adj Close', 'Volume'])

# Calculate ATR
atr_periods = 10
atr_multiplier = 3.0
atr_indicator = AverageTrueRange(high=data['High'], low=data['Low'], close=data['Close'], window=atr_periods)
data['ATR'] = atr_indicator.average_true_range()

# Calculate Up and Down lines
data['hl2'] = (data['High'] + data['Low']) / 2
data['Up'] = data['hl2'] - (atr_multiplier * data['ATR'])
data['Dn'] = data['hl2'] + (atr_multiplier * data['ATR'])

# Initialize trend column
data['Trend'] = np.nan
data['Trend'][0] = 1  # Starting with an uptrend

# Calculate Trend and SuperTrend
for i in range(1, len(data)):
    prev_trend = data['Trend'][i-1]
    prev_up = data['Up'][i-1]
    prev_dn = data['Dn'][i-1]
    close = data['Close'][i-1]
    
    # SuperTrend conditions
    if prev_trend == 1:
        data['Up'][i] = max(data['Up'][i], prev_up)
        if close < data['Up'][i]:
            data['Trend'][i] = -1
        else:
            data['Trend'][i] = 1
    elif prev_trend == -1:
        data['Dn'][i] = min(data['Dn'][i], prev_dn)
        if close > data['Dn'][i]:
            data['Trend'][i] = 1
        else:
            data['Trend'][i] = -1

# Signals
data['BuySignal'] = (data['Trend'] == 1) & (data['Trend'].shift(1) == -1)
data['SellSignal'] = (data['Trend'] == -1) & (data['Trend'].shift(1) == 1)

# Plotting the data
plt.figure(figsize=(14, 8))
plt.plot(data.index, data['Close'], label='Close Price', color='black')
plt.plot(data.index, data['Up'], label='Up Line', color='green')
plt.plot(data.index, data['Dn'], label='Down Line', color='red')
plt.scatter(data.index[data['BuySignal']], data['Up'][data['BuySignal']], marker='^', color='green', label='Buy Signal', s=100)
plt.scatter(data.index[data['SellSignal']], data['Dn'][data['SellSignal']], marker='v', color='red', label='Sell Signal', s=100)
plt.title("SuperTrend Strategy")
plt.legend(loc='best')
plt.show()
