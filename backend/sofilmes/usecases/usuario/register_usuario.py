from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.domain.entities.usuario import Usuario
from typing import Optional


class RegisterUsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def execute(self, usuario: Usuario) -> Optional[Usuario]:
        return self.repository.register(usuario)
