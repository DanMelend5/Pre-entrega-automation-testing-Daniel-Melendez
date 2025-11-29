from pages.inventory_page import InventoryPage


def test_add_to_cart(logged_in_driver):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)

    inventory_page.add_first_product_to_cart()

    # Se verifica si el producto se añadió al carrito
    assert inventory_page.shopping_cart_badge().is_displayed()


