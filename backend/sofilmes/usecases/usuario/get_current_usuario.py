from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.domain.entities.usuario import Usuario
from typing import Optional


class GetCurrentUsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self._repository = repository

    async def execute(self) -> Optional[Usuario]:
        return await self._repository.get_current_usuario()
