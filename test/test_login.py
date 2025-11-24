from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page().login("standard_user", "secret_sauce")

    # Validar redirección
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
