from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



# Configurar Chrome para desactivar alertas de contraseñas y notificaciones
@pytest.fixture(scope="module")
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

    yield driver
    driver.quit()

def test_login(driver):
    #login
        driver.get ("https://www.saucedemo.com/")
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

