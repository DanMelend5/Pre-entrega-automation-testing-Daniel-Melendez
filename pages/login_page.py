from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    #URL
    URL = "https://www.saucedemo.com/"

    _USERNAME= (By.ID, 'user-name')
    _PASSWORD = (By.ID, 'password')
    _LOGIN_BUTTON = (By.ID, 'login-button')
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open_page(self):   
        self.driver.get(self.URL)
        return self
    
    def input_username (self,  username):
        self.wait_for_element(self._USERNAME).send_keys(username)
        return self

    def input_password (self,  password):
        self.wait_for_element(self._PASSWORD).send_keys(password)
        return self

    def click_submit_btn(self):
        self.click(self._LOGIN_BUTTON)
        return self

    def is_error_displayed(self):
        try:
           error = self.wait_for_element(self._ERROR_MESSAGE)
           return error.is_displayed()
        except:
            return False
        
    
    def get_error_message(self):
        if self.is_error_displayed():
            error_text = self.driver.find_element(*self._ERROR_MESSAGE)
            return error_text.text
        return ""


    def login(self, username, password):
        self.input_username(username)
        self.input_password (password)
        self.click_submit_btn()

        #import inventory_page
        from pages.inventory_page import InventoryPage
        return  InventoryPage(self.driver)