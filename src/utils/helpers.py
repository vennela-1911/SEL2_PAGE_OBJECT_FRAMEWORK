import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SCREENSHOT_DIR = "output/screenshots"


def ensure_folder():
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def wait_for(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def click(driver, locator):
    wait_for(driver, locator).click()


def type_text(driver, locator, text):
    element = wait_for(driver, locator)
    element.clear()
    element.send_keys(text)


def capture_screenshot(driver, name):
    ensure_folder()
    timestamp = int(time.time())
    driver.save_screenshot(f"{SCREENSHOT_DIR}/{name}_{timestamp}.png")