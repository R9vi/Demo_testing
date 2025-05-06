import pytest

def test_login(login):
    assert login is not None, "Token was not returned by login API"
    print("Login successful, token received:", login)
