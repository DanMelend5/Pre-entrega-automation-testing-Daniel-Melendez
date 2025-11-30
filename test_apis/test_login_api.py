import pytest
import requests

BASE_URL = "https://reqres.in/api"

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize("payload, expected_status, expect_token", [
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200, True),
    ({"email": "eve.holt@reqres.in"}, 400, False),
])
def test_login_api(payload, expected_status, expect_token, api_headers):
    response = requests.post(
        f"{BASE_URL}/login",
        json=payload,
        headers=api_headers)

    assert response.status_code == expected_status

    json_resp = response.json()

    if expect_token:
        assert "token" in json_resp, "Se esperaba un token y no llegó"
    else:
        assert "token" not in json_resp, "No debería venir token con datos inválidos"