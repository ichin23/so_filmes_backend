import pytest
import datetime
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_crud_filme(client: AsyncClient):
    user_response = await client.post(
        "/usuarios/register",
        json={
            "nome": "Test",
            "username": "username",
            "email": "test@example.com",
            "password": "test@A123",
        },
    )
    assert user_response.status_code == 200
    user_id = user_response.json()["user"]["id"]

    # login
    login_response = await client.post(
        "/usuarios/login",
        json={"email": "test@example.com", "password": "test@A123"},
    )
    token = login_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # criação de filme para avaliar
    filme_response = await client.post(
        "/filme/",
        json={
            "titulo": "O Grande Filme",
            "tituloOriginal": "The Great Movie",
            "capa": "https://example.com/imagens/o-grande-filme.jpg",
            "descricao": "Um filme incrível sobre coragem, amizade e aventura.",
            "avaliacao": 4.7,
            "ano": 2023,
            "generos": ["Aventura", "Drama"],
            "diretor": "João das Neves",
        },
        headers=headers,
    )
    assert filme_response.status_code == 200
    filme_id = filme_response.json()["id"]

    avaliacao_response = await client.post(
        "/avaliacao/",
        json={
            "user_id": user_id,
            "filme_id": filme_id,
            "data": datetime.datetime.now().isoformat(),
            "avaliacao": 5,
            "comentario": "Muito bom",
        },
        headers=headers,
    )

    assert avaliacao_response.status_code == 200
    avaliacao_data = avaliacao_response.json()

    # Buscar todos filmes
    list_filme = await client.get("/filme/", headers=headers)
    assert list_filme.status_code == 200
    list_filme_data = list_filme.json()
    print(list_filme_data)
    assert any(f["titulo"] == "O Grande Filme" for f in list_filme_data)

    # buscar ultimos filmes
    list_filme = await client.get(
        "filme/ultimos",
        headers=headers,
    )
    assert list_filme.status_code == 200
    list_filme_data = list_filme.json()
    assert any(c["titulo"] == "O Grande Filme" for c in list_filme_data)

    # buscar mais avaliados
    list_filme = await client.get(
        "filme/maisAvaliados",
        headers=headers,
    )
    assert list_filme.status_code == 200
    list_filme_data = list_filme.json()
    assert any(c["titulo"] == "O Grande Filme" for c in list_filme_data)

    # bucar filme pelo id
    filme = await client.get(
        f"filme/{filme_id}",
        headers=headers,
    )
    assert filme.status_code == 200
    filme_data = filme.json()
    assert filme_data["titulo"] == "O Grande Filme"
