from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.domain.entities.usuario import Usuario
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password
from typing import Optional


class LoginUsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    async def execute(self, email: Email, senha: Password) -> Optional[Usuario]:
        return await self.repository.login(email, senha)
