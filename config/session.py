import requests
from config.config import BASE_URL, API_KEY, IDENTIFIER, PASSWORD

# session.py

def create_session():
    url = f"{BASE_URL}/session"
    headers = {
        "X-CAP-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "identifier": IDENTIFIER,
        "password": PASSWORD
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        cst, x_security_token = response.headers.get("cst"), response.headers.get("x-security-token")
        
        print("Session created successfully!")  # Add this print statement

        return cst, x_security_token
    else:
        raise Exception(f"Failed to create session: {response.status_code} {response.text}")
