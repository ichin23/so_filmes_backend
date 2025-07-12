from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository


class LogoutUsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    async def execute(self) -> None:
        await self.repository.logout()
