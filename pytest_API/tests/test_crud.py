import pytest
from utils.api_utils import create_user, get_user, update_user, delete_user
from utils.test_data import USER_DATA, UPDATED_USER_DATA

def test_create_data(login, headers):
    response = create_user(USER_DATA, headers)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    assert 'id' in response.json(), "Response does not contain 'id' field"
    print("Data created successfully:", response.json())

def test_get_data(login, headers):
    response = get_user(1, headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert 'data' in response.json(), "Response does not contain 'data' field"
    print("Data fetched successfully:", response.json())

def test_update_data(login, headers):
    response = update_user(2, UPDATED_USER_DATA, headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()['name'] == UPDATED_USER_DATA['name'], "Name not updated"
    print("Data updated successfully:", response.json())

def test_delete_data(login, headers):
    response = delete_user(2, headers)
    assert response.status_code == 204, f"Expected 204, got {response.status_code}"
    print("Data deleted successfully.")
