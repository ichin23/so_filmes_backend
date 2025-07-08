from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository


class LogoutUsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def execute(self) -> None:
        self.repository.logout()
