import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_single_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == post_id
    assert "title" in json_data
    assert "body" in json_data

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == "foo"
    assert json_data["body"] == "bar"
