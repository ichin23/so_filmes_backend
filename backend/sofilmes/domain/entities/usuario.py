from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password


class Usuario:
    def __init__(
        self,
        id: str,
        nome: str,
        username: str,
        email: Email,
        senha: Password,
        media: float = 0,
    ):
        self.id = id
        self.nome = nome
        self.username = username
        self.email = email
        self.senha = senha
        self.media = media
