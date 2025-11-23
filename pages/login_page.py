from .base_page import BasePage
from selenium.webdriver.common.by import By

class logingPage(BasePage):
    #URL
    URL = "https://www.saucedemo.com/"

    _USERNAME= (By.ID, 'user-name')
    _PASSWORD = (By.ID, 'password')
    _LOGIN_BUTTON = (By.ID, 'login-button')

    def open_page(self):   
        self.driver.get(self.URL)
        return self
    
    def input_user (self,  username):
        self.wait_for_element(self._USERNAME).send_keys(username)
        return self

    def input_password (self,  password):
        self.wait_for_element(self._PASSWORD).send_keys(password)
        return self

    def click_submit_btn(self):
        self.click(self._LOGIN_BUTTON)

    def login(self, username, password):
        self.input_user(username)
        self.input_password (password)
        self.click_submit_btn()
        return self