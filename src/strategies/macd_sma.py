import pandas as pd
import yfinance as yf
from ta.utils import dropna
from ta.trend import MACD, EMAIndicator, SMAIndicator

# Load and preprocess data
def preprocess_data():
    data = yf.download("EURUSD=x", period="5d", interval="1h")
    data.index = pd.to_datetime(data.index)
    data = data.drop(columns=['Adj Close', 'Volume'])
    data = dropna(data)

    # Initialize MACD Indicator
    indicator_macd = MACD(close=data["Close"], window_slow=26, window_fast=12, window_sign=9)
    data['macd'] = indicator_macd.macd()
    data['signal'] = indicator_macd.macd_signal()
    data['hist'] = indicator_macd.macd_diff()

    # Initialize EMA Indicator
    indicator_ema = EMAIndicator(close=data["Close"], window=20)
    data['ema'] = indicator_ema.ema_indicator()

    # Initialize SMA Indicator
    indicator_sma = SMAIndicator(close=data["Close"], window=20)
    data['sma'] = indicator_sma.sma_indicator()

    return data

# Define the trading strategy
def trading_strategy(data):
    position = 0  # 0 means no position, 1 means long, -1 means short
    entry_price = 0
   
    for i in range(1, len(data)):
        if position == 0:
            # Check for long entry
            if data['macd'].iloc[i] > data['signal'].iloc[i] and data['Close'].iloc[i] > data['sma'].iloc[i]:
                position = 1
                entry_price = data['Close'].iloc[i]
                print(f"Entering long at {entry_price} on {data.index[i]}")
            # Check for short entry
            elif data['macd'].iloc[i] < data['signal'].iloc[i] and data['Close'].iloc[i] < data['sma'].iloc[i]:
                position = -1
                entry_price = data['Close'].iloc[i]
                print(f"Entering short at {entry_price} on {data.index[i]}")
        elif position == 1:
            # Check for long exit
            if data['macd'].iloc[i] < data['signal'].iloc[i] or (data['Close'].iloc[i] / entry_price - 1):
                position = 0
                print(f"Exiting long at {data['Close'].iloc[i]} on {data.index[i]}")
        elif position == -1:
            # Check for short exit
            if data['macd'].iloc[i] > data['signal'].iloc[i] or (entry_price / data['Close'].iloc[i] - 1):
                position = 0
                print(f"Exiting short at {data['Close'].iloc[i]} on {data.index[i]}")

        data.at[data.index[i], 'position'] = position

    return data

# Run the backtest
if __name__ == "__main__":
    data = preprocess_data()
    results = trading_strategy(data)



