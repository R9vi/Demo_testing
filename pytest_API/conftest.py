import pytest
import requests

# Base URL for ReqRes API
BASE_URL = "https://reqres.in/api"
LOGIN_URL = f"{BASE_URL}/login"
TOKEN = None

@pytest.fixture(scope="module")
def headers():
    return {
        "x-api-key": "reqres-free-v1"
    }

@pytest.fixture(scope="module")
def login_data():
    return {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

@pytest.fixture(scope="module")
def login(login_data, headers):
    global TOKEN
    response = requests.post(LOGIN_URL, json=login_data, headers=headers)
    if response.status_code == 200:
        TOKEN = response.json().get('token')
    else:
        pytest.fail("Login failed")
    return TOKEN
