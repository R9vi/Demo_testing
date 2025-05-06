from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self, username):
        self.driver.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def get_error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert')]").text
        except:
            return None

    def get_warning_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//*[contains(@class, 'oxd-form-row')]//span").text
        except:
            return None