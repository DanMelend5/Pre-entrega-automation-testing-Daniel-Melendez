import pytest
from selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
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
    driver.implicitly_wait(5) #tiempo de espera implicito 

    yield driver #yield =="@Aftermetho()"  in fixtures with pytests
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver



#El conftest se reconcen automaticamente en las fixtures