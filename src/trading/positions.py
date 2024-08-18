import requests
from config.config import BASE_URL

def get_all_postions(cst, x_security_token):
    url = f"{BASE_URL}/postions"
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