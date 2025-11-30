import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

#from pages.login_page import LoginPage
#from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture 
def logged_in_driver(driver):
    LoginPage(driver).open_page().login("standard_user", "secret_sauce")
    return driver



@pytest.fixture
def api_headers():
    return {"x-api-key": "reqres-free-v1"}
