from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



# Configurar Chrome para desactivar alertas de contraseñas y notificaciones
chrome_options = Options()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5) #tiempo de espera implicito 


try:
    #login
        driver.get ("https://www.saucedemo.com/")
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        #time.sleep(5)

    # validacion de la redirection de la pagina
        assert '/inventory.html' in driver.current_url

    # validacion titulo
        titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
        print(titulo)

        """   # Interacciones
        productos = driver.find_elements(By.CLASS_NAME, "inventory-item")
        productos[0].find_element(By.TAG_NAME, "button").click()
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text()
        assert carrito == "1" """

        print("Test OK")

finally:
    driver.quit