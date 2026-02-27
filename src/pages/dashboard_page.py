from selenium.webdriver.common.by import By
from src.utils.helpers import click


class DashboardPage:

    LOGOUT_BTN = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        self.driver = driver

    def is_logged_in(self):
        return "logged-in-successfully" in self.driver.current_url

    def logout(self):
        click(self.driver, self.LOGOUT_BTN)
        
        