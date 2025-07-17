import pytest


@pytest.mark.asyncio
async def test_register_and_login(client):
    # Registro
    response = await client.post(
        "/usuarios/register",
        json={
            "nome": "Test",
            "username": "username",
            "email": "test@example.com",
            "password": "test@A123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User Registered Successfully"

    # Login
    response = await client.post(
        "/usuarios/login", json={"email": "test@example.com", "password": "test@A123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    token = data["access_token"]

    # GET /usuarios/me
    response = await client.get(
        "/usuarios/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
