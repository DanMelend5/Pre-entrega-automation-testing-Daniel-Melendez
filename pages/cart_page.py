from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    _PRODUCT_NAME_IN_CART = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_IN_CART = (By.CLASS_NAME, "cart_item")
    _REMOVE_ITEM_BUTTON = (By.TAG_NAME, "button")
    _CONTINUE_SHOPPING = (By.ID, "continue-shopping")