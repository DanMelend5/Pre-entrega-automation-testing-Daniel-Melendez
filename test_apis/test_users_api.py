
import pytest
import requests

BASE_URL = "https://reqres.in/api"

@pytest.mark.api
@pytest.mark.smoke
def test_users_api(api_headers):
    response = requests.get(f"{BASE_URL}/users?page=1", headers=api_headers)

    assert response.status_code == 200

    data = response.json()["data"]

    for user in data:
        # Validar claves
        for key in ["id", "email", "first_name", "last_name"]:
            assert key in user, f"Falta {key} en usuario: {user}"
