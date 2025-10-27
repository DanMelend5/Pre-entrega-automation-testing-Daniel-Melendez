import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from utils import login
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


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
    #driver.implicitly_wait(5) #tiempo de espera implicito 

    yield driver #yield =="@Aftermetho()"  in fixtures with pytests
    driver.quit()


@pytest.fixture
def wait(driver: WebDriver):
    return WebDriverWait(driver, 6)

@pytest.fixture
def wait_for_element(wait):
    def _wait_for_element(locator):
        return wait.until(EC.visibility_of_element_located(locator))
    return _wait_for_element

@pytest.fixture
def wait_for_invisibility(wait):
    def _wait_for_invisibility(locator):
        return wait.until(EC.invisibility_of_element_located(locator))
    return _wait_for_invisibility

@pytest.fixture
def login_in_driver(driver: WebDriver):
    login(driver)
    return driver




#El conftest se reconcen automaticamente en las fixtures