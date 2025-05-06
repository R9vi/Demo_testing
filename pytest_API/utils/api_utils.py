import requests

BASE_URL = "https://reqres.in/api"

def create_user(data, headers):
    url = f"{BASE_URL}/users"
    response = requests.post(url, json=data, headers=headers)
    return response

def get_user(user_id, headers):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url, headers=headers)
    return response

def update_user(user_id, data, headers):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.put(url, json=data, headers=headers)
    return response

def delete_user(user_id, headers):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.delete(url, headers=headers)
    return response
