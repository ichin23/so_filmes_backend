import pytest
import datetime
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_crud_avaliacao(client: AsyncClient):

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

    # criação de avaliação
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

    assert avaliacao_data["user_id"] == user_id
    assert avaliacao_data["filme_id"] == filme_id
    assert avaliacao_data["avaliacao"] == 5
    assert avaliacao_data["comentario"] == "Muito bom"

    # Buscar avaliação por usuario
    list_avaliacao = await client.get(
        f"/avaliacao/byuser",
        headers=headers,
    )
    assert list_avaliacao.status_code == 200
    list_avaliacao_data = list_avaliacao.json()
    assert any(c["comentario"] == "Muito bom" for c in list_avaliacao_data)

    # Buscar avaliação por filme
    list_avaliacao = await client.get(
        f"/avaliacao/byfilme/{filme_id}",
        headers=headers,
    )
    assert list_avaliacao.status_code == 200
    list_avaliacao_data = list_avaliacao.json()
    assert any(c["comentario"] == "Muito bom" for c in list_avaliacao_data)

    # Buscar avaliação por id
    list_avaliacao = await client.get(
        f"/avaliacao/byid/{avaliacao_data['id']}",
        headers=headers,
    )
    assert list_avaliacao.status_code == 200
    list_avaliacao_data = list_avaliacao.json()
    assert list_avaliacao_data["comentario"] == "Muito bom"

    # Buscar ultimas avalições
    list_avaliacao = await client.get(
        f"/avaliacao/ultimas",
        headers=headers,
    )
    assert list_avaliacao.status_code == 200
    list_avaliacao_data = list_avaliacao.json()
    assert any(c["comentario"] == "Muito bom" for c in list_avaliacao_data)

    # Editar avaliação
    avaliacao = await client.put(
        f"/avaliacao/{ avaliacao_data['id']}",
        json={
            "user_id": user_id,
            "filme_id": filme_id,
            "data": datetime.datetime.now().isoformat(),
            "avaliacao": 4,
            "comentario": "Muito bom, mas poderia ser melhor",
        },
        headers=headers,
    )
    assert avaliacao.status_code == 200
    avaliacao_data = avaliacao.json()
    assert avaliacao_data["comentario"] == "Muito bom, mas poderia ser melhor"

    # Deletar avaliação
    avaliacao = await client.delete(
        f"/avaliacao/{ avaliacao_data['id']}",
        headers=headers,
    )
    assert avaliacao.status_code == 200
    avaliacao_data = avaliacao.json()
    assert avaliacao_data["message"] == "Avaliação deletada com sucesso"
