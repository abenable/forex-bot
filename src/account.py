# account.py
import requests
from config.config import BASE_URL

def get_account_info(cst, x_security_token):
    url = f"{BASE_URL}/accounts"
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
    
def get_account_activity_history(cst, x_security_token):
    url = f"{BASE_URL}/history/activity"
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
    
def get_account_transaction_history(cst, x_security_token):
    url = f"{BASE_URL}/history/transactions"
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
