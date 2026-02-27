from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage


def test_logout(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()
    login.login("student", "Password123")
    dashboard.logout()

    assert "practice-test-login" in driver.current_url