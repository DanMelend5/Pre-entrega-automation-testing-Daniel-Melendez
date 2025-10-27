def test_login(login_in_driver):
    try:
        driver = login_in_driver
        # validacion de la redirection de la pagina
        assert '/inventory.html' in driver.current_url, "no se redidirio al inventario"

        print("login exitoso")

    except Exception as e:
        print(f"error en test login: {e}")
        raise