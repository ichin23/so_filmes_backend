from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.domain.entities.usuario import Usuario


class SetCurrentUsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    async def execute(self, usuario: Usuario) -> None:
        await self.repository.set_current_usuario(usuario)
