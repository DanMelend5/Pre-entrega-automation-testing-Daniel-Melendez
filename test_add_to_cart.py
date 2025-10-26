from selenium import webdriver
from selenium.webdriver.common.by import By



def test_add_to_cart(login_in_driver):
    try:
        driver = login_in_driver
    
        items_pricebar = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(items_pricebar) > 0, "No se encontraron productos"

        items_pricebar = driver.find_elements(By.CLASS_NAME, "inventory_item")
        items_pricebar[0].find_element(By.TAG_NAME, "button").click()
        #shopping_cart_batch = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text()
        #assert shopping_cart_batch == "1"

        
        """
        add_to_cart_buttons = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_buttons.click()
        
        """        




        
    except Exception as e:
        print(f"error en test inventory: {e}")
        raise