from .base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _ADD_TO_CART_BUTTON = (By.TAG_NAME, "button")
    _SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_products(self):
        return self.wait_for_all_elements(self._PRODUCTS)

    def get_product_names(self):
        return [p.text for p in self.wait_for_all_elements(self._PRODUCT_NAME)]

    def get_product_prices(self):
        return [p.text for p in self.wait_for_all_elements(self._PRODUCT_PRICE)]
    
    def add_first_product_to_cart(self):
        products = self.get_products()
        first_product = products[0]
        add_button = first_product.find_element(*self._ADD_TO_CART_BUTTON)
        add_button.click()

    def click_shopping_cart_badge(self):
        self.click(self._SHOPPING_CART_BADGE)
        from cart_page import CartPage
        return CartPage(self.driver)

    def shopping_cart_badge(self):
        return self.wait_for_element(self._SHOPPING_CART_BADGE)