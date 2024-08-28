import requests
from config.config import BASE_URL


def get_all_orders(cst, x_security_token):
    url = f"{BASE_URL}/workingorders"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        raise Exception(f"Failed to retrieve orders info: {response.status_code} {response.text}")

def print_all_orders(response):
    data = response.json()
    orders = data.get('orders', [])

    # Print the header
    print("Open orders")
    print(f"{'Order':<7} {'Symbol':<10} {'Size':<10} {'Direction':<10} {'OpenPrice':<10} {'TakeProfit':<12} {'StopLoss':<10} {'Profit/Loss':<10}")
    print("-" * 85)

    # Print each item in the formatted table
    for item in orders:
        if item:  # Check if item is not null
            order = item.get('order', {})
            market = item.get('market', {})
            
            dealId = orders.index(item) + 1
            symbol = market.get('symbol', 'N/A')
            size = order.get('size', 'N/A')
            direction = order.get('direction', 'N/A')
            openPrice = order.get('level', 'N/A')
            tp = order.get('profitLevel', 'N/A')
            sl = order.get('stopLevel', 'N/A')
            P_L = order.get('upl', 'N/A')
            
            print(f"{dealId:<7} {symbol:<10} {size:<10} {direction:<10} {openPrice:<10} {tp:<12} {sl:<10} {P_L:<10}")

 
def create_order(cst, x_security_token, data):
    url = f"{BASE_URL}/workingorders"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    data = {
        "direction": data.direction,
        "epic": data.epic,
        "size": data.size,
        "type":data.type,
        "level":data.level,
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to create order: {response.status_code} {response.text}")

def update_order_byId(id, cst, x_security_token,data):
    url = f"{BASE_URL}/workingorders/{id}"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
    data = {
        "epic": data.epic,
        "level":data.level,
    }
    response = requests.put(url, json=data, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to update order: {response.status_code} {response.text}")
    
def delete_order_byId(id, cst, x_security_token):
    url = f"{BASE_URL}/workingorders/{id}"
    headers = {
        "cst": cst,
        "x-security-token": x_security_token,
        "Content-Type": "application/json"
    }
  

    response = requests.delete()(url, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to update order: {response.status_code} {response.text}")