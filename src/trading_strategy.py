# trading_strategy.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ta
import requests
import json
import time
from config.config import BASE_URL

def get_price_history(epic,resolution, start, end,max, cst, x_security_token):
    url = f"{BASE_URL}/prices/{epic}?resolution={resolution}&from={start}&to={end}&max={max}"

    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    
    while True:
        response = json.loads(requests.get(url, headers=headers))
    
        if response.status_code == 200:
            # Extract prices
            prices = response['prices']
    
            # Convert to DataFrame
            df = pd.DataFrame(prices)
    
            # Convert 'snapshotTime' to datetime
            df['snapshotTime'] = pd.to_datetime(df['snapshotTime'])
    
            # Set 'snapshotTime' as the index
            df.set_index('snapshotTime', inplace=True)
    
            # Normalize nested dictionary fields
            df['openPrice_bid'] = df['openPrice'].apply(lambda x: x['bid'])
            df['closePrice_bid'] = df['closePrice'].apply(lambda x: x['bid'])
            df['highPrice_bid'] = df['highPrice'].apply(lambda x: x['bid'])
            df['lowPrice_bid'] = df['lowPrice'].apply(lambda x: x['bid'])
    
            # Drop the original nested columns
            df.drop(columns=['openPrice', 'closePrice', 'highPrice', 'lowPrice'], inplace=True)
    
            # Display the DataFrame
            print(df.head())

            # Calculate SMAs
            df['SMA_10'] = ta.trend.sma_indicator(df['closePrice_bid'], window=10)
            df['SMA_30'] = ta.trend.sma_indicator(df['closePrice_bid'], window=30)

            # Define a simple trading signal
            def trading_signal(row):
                if pd.notna(row['SMA_10']) and pd.notna(row['SMA_30']):
                    if row['SMA_10'] > row['SMA_30']:
                        return "Buy"
                    elif row['SMA_10'] < row['SMA_30']:
                        return "Sell"
                return "Hold"

            df['Signal'] = df.apply(trading_signal, axis=1)

            # Plotting the results

            plt.figure(figsize=(14, 7))
            plt.plot(df.index, df['closePrice_bid'], label='Close Price', alpha=0.5)
            plt.plot(df.index, df['SMA_10'], label='SMA 10', alpha=0.75)
            plt.plot(df.index, df['SMA_30'], label='SMA 30', alpha=0.75)
            plt.title('Close Price and Moving Averages')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.show()
            
        else:
            raise Exception(f"Failed to retrieve watchlist info: {response.status_code} {response.text}")

def execute_trading_strategy(api, cst, x_security_token):
    # Example strategy implementation
    account_info = api.get_account_info(cst, x_security_token)
    # Implement your strategy here
    print("Executing trading strategy with account info:", account_info)
