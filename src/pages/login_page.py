from selenium.webdriver.common.by import By
from src.utils.helpers import type_text, click, wait_for
from src.utils.decorators import capture_screenshot_on_fail


class LoginPage:

    URL = "https://practicetestautomation.com/practice-test-login/"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "submit")
    ERROR_MSG = (By.ID, "error")   # ✅ Correct locator

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    @capture_screenshot_on_fail
    def login(self, username, password):
        type_text(self.driver, self.USERNAME, username)
        type_text(self.driver, self.PASSWORD, password)
        click(self.driver, self.LOGIN_BTN)

    def get_error_message(self):
        return wait_for(self.driver, self.ERROR_MSG).text.strip()