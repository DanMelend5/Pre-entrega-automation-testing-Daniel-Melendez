from selenium import webdriver
from selenium.webdriver.common.by import By


def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
        # validacion de la redirection de la pagina
        assert driver.title =="Swag labs"


        products = driver.find_elements(By.CLASS_NAME, "inventory_items")
        assert len(products) > 0, "no hay productos visibles en la pagina"
    
    except Exception as e:
        print(f"error en test inventory: {e}")
        raise
    finally: 
        driver.quit()    