from pages.inventory_page import InventoryPage


def test_inventory(logged_in_driver):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)

    assert driver.title == "Swag Labs"

    product_names = inventory_page.get_product_names()

    # Validar primer producto
    assert product_names[0] == "Sauce Labs Backpack", "El nombre del producto es incorrecto"
