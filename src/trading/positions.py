import os
import time
from turtle import position
import requests
from config.config import BASE_URL

def clear_console():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def get_all_postions(cst, x_security_token):
    url = f"{BASE_URL}/positions"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    
    while True:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            positions = data.get('positions', [])

            # Clear the console before printing new data
            clear_console()

            # Print the header
            print(f"{'Pos':<7} {'Symbol':<10} {'Size':<10} {'Direction':<10} {'OpenPrice':<10} {'TakeProfit':<10} {'StopLoss':<10} {'Profit/Loss':<10}")
            print("-" * 85)

            # Print each item in the formatted table
            for item in positions:
                if item:  # Check if item is not null
                    position = item.get('position', {})
                    market = item.get('market', {})
                    
                    dealId = positions.index(item) + 1
                    symbol = market.get('symbol', 'N/A')
                    size = position.get('size', 'N/A')
                    direction = position.get('direction', 'N/A')
                    openPrice = position.get('level', 'N/A')
                    tp = position.get('profitLevel', 'N/A')
                    sl = position.get('stopLevel', 'N/A')
                    P_L = position.get('upl', 'N/A')
                    
                    print(f"{dealId:<7} {symbol:<10} {size:<10} {direction:<10} {openPrice:<10} {tp:<10} {sl:<10} {P_L:<10}")

            # Wait before updating the table again
            time.sleep(1)
        else:
            raise Exception(f"Failed to retrieve account info: {response.status_code} {response.text}")
    
def get_postion_byId(id, cst, x_security_token):
    url = f"{BASE_URL}/postions/{id}"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve account info: {response.status_code} {response.text}")


def create_position(cst, x_security_token, direction, epic, size, guaranteedStop=False, trailingStop=False, 
                    stopLevel=None, stopDistance=None, stopAmount=None, profitLevel=None, 
                    profitDistance=None, profitAmount=None):
    url = f"{BASE_URL}/positions"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    payload = {
        "direction": direction,
        "epic": epic,
        "size": size,
        "guaranteedStop": guaranteedStop,
        "trailingStop": trailingStop,
        "stopLevel": stopLevel,
        "stopDistance": stopDistance,
        "stopAmount": stopAmount,
        "profitLevel": profitLevel,
        "profitDistance": profitDistance,
        "profitAmount": profitAmount
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to create position: {response.status_code} {response.text}")

def update_position_byId(id, cst, x_security_token, guaranteedStop=False, trailingStop=False, 
                    stopLevel=None, stopDistance=None, stopAmount=None, profitLevel=None, 
                    profitDistance=None, profitAmount=None):
    url = f"{BASE_URL}/positions/{id}"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    payload = {
        "guaranteedStop": guaranteedStop,
        "trailingStop": trailingStop,
        "stopLevel": stopLevel,
        "stopDistance": stopDistance,
        "stopAmount": stopAmount,
        "profitLevel": profitLevel,
        "profitDistance": profitDistance,
        "profitAmount": profitAmount
    }

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to update position: {response.status_code} {response.text}")
    
def close_position_byId(id, cst, x_security_token, ):
    url = f"{BASE_URL}/positions/{id}"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
  

    response = requests.delete()(url, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to update position: {response.status_code} {response.text}")