from pages.inventory_page import InventoryPage


def test_inventory(logged_in_driver):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)

    assert driver.title == "Swag Labs"


    products = inventory_page.get_products()
    product_names = inventory_page.get_product_names()
    product_prices = inventory_page.get_product_prices()

    
    # Validar primer producto
    assert product_names[0] == "Sauce Labs Backpack", "El nombre del producto es incorrecto"
    assert product_prices[0] == '$29.99', "El precio del producto es incorrecto"
    assert len(products) > 0, "No se encontraron productos"

