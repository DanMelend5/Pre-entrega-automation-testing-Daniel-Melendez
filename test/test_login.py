from pages.login_page import LoginPage
import pytest
from utils.data import read_csv_login

# Cargar casos de prueba desde CSV
TEST_CASE_LOGIN = read_csv_login('data\login.csv')


@pytest.mark.parametrize("username, password, valid_credentials, description", TEST_CASE_LOGIN)
def test_login_from_cvs(driver, username, password, valid_credentials, description):
    login_page = LoginPage(driver)
    login_page.open_page()  

    login_page.login(username, password)

    if valid_credentials:
    # Validar redirección
        assert "/inventory.html" in driver.current_url, "{username} cannot login."
        print(description)

    
    else:
        # Login fallido: debe mostrar error

        assert login_page.is_error_displayed(), f"{username} did not displayed error message"
        error_message = login_page.get_error_message()
        assert len(error_message) > 0, "El mensaje de error está vacío"
        print(f" Login falló correctamente - Error: {error_message}")


@pytest.mark.smoke
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page()  
    login_page.login("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url, "cannot login."
        