import requests
import os
import time
from config.config import BASE_URL


def get_watchlist(id, cst, x_security_token):
    url = f"{BASE_URL}/watchlists/{id}"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        raise Exception(f"Failed to retrieve watchlist info: {response.status_code} {response.text}")
    
def print_watchlist(response):
    data = response.json()
    markets = data.get('markets', [])

    # Print the header
    print("Watchlist")
    print(f"{'Symbol':<10} {'Bid':<10} {'Offer':<10} {'High':<10} {'Low':<10} {'Change':<10}")
    print("-" * 61)

    # Print each item in the formatted table
    for item in markets:
        if item:  # Check if item is not null
            symbol = item.get('symbol', 'N/A')
            high = item.get('high', 'N/A')
            low = item.get('low', 'N/A')
            bid = item.get('bid', 'N/A')
            offer = item.get('offer', 'N/A')
            change = item.get('percentageChange', 'N/A')
            print(f"{symbol:<10}  {bid:<10} {offer:<10} {high:<10} {low:<10} {change:<10}")