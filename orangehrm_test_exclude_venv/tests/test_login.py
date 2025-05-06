import pytest
import json
from pages.login_page import LoginPage

# @pytest.mark.parametrize("cred_type", ["valid", "invalid", "empty"])
# def test_login(driver, cred_type):
#     with open("testdata/credentials.json") as f:
#         data = json.load(f)[cred_type]
#
#     login = LoginPage(driver)
#     login.load()
#     login.enter_username(data["username"])
#     login.enter_password(data["password"])
#     login.click_login()
#
#     if cred_type == "valid":
#         assert "dashboard" in driver.current_url.lower()
#     elif cred_type == "empty":
#         assert login.get_warning_message() is not None
#     else:
#         assert login.get_error_message() is not None

def test_valid_login(driver):
    with open("testdata/credentials.json") as f:
        data = json.load(f)["valid"]

    login = LoginPage(driver)
    login.load()
    login.enter_username(data["username"])
    time.sleep(2)
    login.enter_password(data["password"])
    time.sleep(2)
    login.click_login()

    assert "dashboard" in driver.current_url.lower(), "Valid login failed to reach dashboard"


def test_invalid_login(driver):
    with open("testdata/credentials.json") as f:
        data = json.load(f)["invalid"]

    login = LoginPage(driver)
    login.load()
    login.enter_username(data["username"])
    time.sleep(2)
    login.enter_password(data["password"])
    time.sleep(2)
    login.click_login()

    error_message = login.get_error_message()
    assert error_message is not None and "Invalid" in error_message, "Expected error message not found for invalid login"


def test_empty_credentials(driver):
    with open("testdata/credentials.json") as f:
        data = json.load(f)["empty"]

    login = LoginPage(driver)
    login.load()
    login.enter_username(data["username"])
    time.sleep(2)
    login.enter_password(data["password"])
    time.sleep(2)
    login.click_login()

    error_message = login.get_warning_message()
    assert error_message is not None, "Expected error for empty credentials not displayed"

