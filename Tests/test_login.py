from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage


def test_valid_login(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()
    login.login("student", "Password123")

    assert dashboard.is_logged_in()


def test_invalid_username(driver):
    login = LoginPage(driver)

    login.open()
    login.login("wrongUser", "Password123")

    assert login.get_error_message() == "Your username is invalid!"


def test_invalid_password(driver):
    login = LoginPage(driver)

    login.open()
    login.login("student", "wrongPass")

    assert login.get_error_message() == "Your password is invalid!"