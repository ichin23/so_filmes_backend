from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password


class Usuario:
    def __init__(
        self, id: str, nome: str, username: str, email: Email, senha: Password
    ):
        self.id = id
        self.nome = nome
        self.username = username
        self.email = email
        self.senha = senha
