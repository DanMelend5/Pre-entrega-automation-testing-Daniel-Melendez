from selenium import webdriver
from selenium.webdriver.common.by import By


def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
        # validacion de la redirection de la pagina
        assert driver.title =="Swag Labs"

        item_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        item_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        
        assert item_name[0].text == 'Sauce Labs Backpack', "Error en el nombre, el precio correcto es: {item_name}"
        assert item_price[0].text == '$29.99', "Error en el precio, el precio correcto es: {item_price}"

    
    except Exception as e:
        print(f"error en test inventory: {e}")
        raise