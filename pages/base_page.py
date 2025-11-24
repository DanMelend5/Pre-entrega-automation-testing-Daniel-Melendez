from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage: 

    def __init__(self, driver,):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_invisibility(self, locator):
        return  self.waitwait.until(EC.invisibility_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()
