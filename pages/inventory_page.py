from .base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def get_product_names(self):
        elements = self.wait_for_all_elements(self.PRODUCT_NAME)
        return [el.text for el in elements]

    def get_product_prices(self):
        elements = self.wait_for_all_elements(self.PRODUCT_PRICE)
        return [el.text for el in elements]
