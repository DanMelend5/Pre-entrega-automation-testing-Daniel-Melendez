import pytest

#lista de archios pruebas a ejecutar

test_files = [
    "test/test_login.py",
    "test/test_inventory.py",

]


# usa los comando para correr

pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)