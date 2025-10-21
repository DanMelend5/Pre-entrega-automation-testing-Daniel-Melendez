from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver
        # validacion de la redirection de la pagina
        assert '/inventory.html' in driver.current_url, "no se redidirio al inventario"

    except Exception as e:
        print(f"error en test login: {e}")
        raise
    finally: 
        driver.quit()