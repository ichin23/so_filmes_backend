import pytest
from sofilmes.domain.entities.usuario import Usuario
from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password

def test_create_user():
    email = Email("user@example.com")
    pwd = Password("Secret123")
    user = Usuario("1", "User", email, pwd, "user")
    assert user.nome == "User"

def test_create_avaliacao():
    avaliacao = Avaliacao("1", 4, "Filme Otimo", "1")
    assert avaliacao.comentario == "Filme Otimo"