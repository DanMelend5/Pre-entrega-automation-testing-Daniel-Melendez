import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
#from utils import login
from pages.login_page import logingPage
from selenium.webdriver.chrome.options import Options



@pytest.fixture
# Configurar Chrome para desactivar alertas de contraseñas y notificaciones
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
def login_in_driver(driver):
    logingPage(driver).open_page().login("standard_user", "secret_sauce")
    return driver


#El conftest se reconcen automaticamente en las fixtures