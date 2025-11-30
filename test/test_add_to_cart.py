import pytest
from pages.inventory_page import InventoryPage
from utils.data import read_json_products


# Carga productos desde JSON
PRODUCTS_JSON = read_json_products('data\SwagLabsProducts.json')



    # verifica si se puede añadir el primer producto al carrito
def test_add_to_cart(logged_in_driver):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)

    inventory_page.add_first_product_to_cart()

    # Se verifica si el producto se añadió al carrito
    assert inventory_page.is_shopping_cart_badge_display()

@pytest.mark.parametrize("product_data", PRODUCTS_JSON)
def test_agregar_producto_desde_json(logged_in_driver, product_data):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)
    product_name = product_data["name"]

    inital_badge_counter = inventory_page.shopping_cart_counter()
    if  inital_badge_counter > 0:
        print(f"hay {inital_badge_counter} productos agregados.")
    else:  print(f"No hay productos agregados.")
    
    # Agregar producto específico
    inventory_page.add_product_to_cart_by_name(product_name)
    
    # Verificar que el contador se incrementó
    final_badge_counter = inventory_page.shopping_cart_counter()
    print(f"   Contador final: {final_badge_counter}")
    
    assert final_badge_counter == inital_badge_counter + 1, \
        f"El contador no se incrementó correctamente para {product_name}"
    
    print(f"   ✅ Producto agregado correctamente")