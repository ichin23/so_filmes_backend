from sofilmes.domain.entities.filme import Filme
from sofilmes.domain.entities.usuario import Usuario
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password
import uuid
from sofilmes.domain.entities.avaliacao import Avaliacao

def test_create_usuario() -> Usuario:
    usuario = Usuario(
        id=str(uuid.uuid4()),
        nome="Test Usuario",
        email=Email("test@example.com"),
        senha=Password("secur3Pass"),
        username="usuario"
    )
    assert usuario.nome =="Test Usuario"

def test_create_filme():
    filme =  Filme(
        id=str(uuid.uuid4()),
        titulo="Filme 1",
        tituloOriginal="Movie 1",
        ano=2025,
        avaliacao=5,
        capa="",
        descricao="Um filme com imagens",
        diretor="Nolan",
        generos=["Ação"],
    )
    assert filme.titulo == "Filme 1"

def test_create_avaliacao():
    avaliacao = Avaliacao(
        id=str(uuid.uuid4()),
        autor_id=str(uuid.uuid4()),
        filme_id=str(uuid.uuid4()),
        avaliacao=5,
        comentario="Muito bom"
    )

    assert avaliacao.avaliacao == 5
    assert avaliacao.comentario == "Muito bom"