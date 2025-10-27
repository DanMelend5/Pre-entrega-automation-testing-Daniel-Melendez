from selenium import webdriver
from selenium.webdriver.common.by import By




def test_add_to_cart(login_in_driver, wait_for_element, wait_for_invisibility):
    try:
        #Se encuentra el primer producto y se añade al carrito
        driver = login_in_driver
        products= driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos"
        product_name = products[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
        add_to_cart_bttn = products[0].find_element(By.TAG_NAME, "button")
        add_to_cart_bttn.click()

        # Se verifica si el producto se añadió al carrito
        shopping_cart_badge = wait_for_element((By.CLASS_NAME, "shopping_cart_badge"))
        assert shopping_cart_badge.is_displayed()

        # Se verifica si el producto se añadadido al carrito corresponde con producto seleccionado originalmente
        shopping_cart_badge.click()
        product_name_in_cart = wait_for_element ((By.CLASS_NAME, "inventory_item_name"))
        assert product_name_in_cart.text == product_name

        #Se verifica si el producto seleccionado se eliminó 
        product_in_cart = wait_for_element((By.CLASS_NAME, "cart_item"))
        remove_item_button = product_in_cart.find_element(By.TAG_NAME, "button")
        remove_item_button.click()
    
        assert wait_for_invisibility((By.CLASS_NAME, "cart_item")), " El producto {product_in_cart} no se eliminó correctamente"

        
    except Exception as e:
        print(f"error en test inventory: {e}")
        raise