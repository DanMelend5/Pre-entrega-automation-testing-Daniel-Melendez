import pytest

#lista de archios pruebas a ejecutar

test_files = [
    "test/test_login.py",
    "test/test_inventory.py",
    "test/test_add_to_cart.py",
    "test_apis/test_login_api.py",
    "test_apis/test_users_api.py"
]


# usa los comando para correr

pytest_args = test_files + ["--html=TalentoLab.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)



