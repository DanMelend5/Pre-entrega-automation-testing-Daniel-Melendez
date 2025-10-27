from selenium.webdriver.common.by import By


def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
        # validacion de la redirection de la pagina
        assert driver.title =="Swag Labs"

        product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        
        assert product_name[0].text == 'Sauce Labs backpack', "El nombre del producto es incorrecto"
        assert product_price[0].text == '$29.99', "El precio del producto es incorrecto"

        print("prueba exitosa")

    except Exception as e:
        print(f"error en test inventory: {e}")
        raise