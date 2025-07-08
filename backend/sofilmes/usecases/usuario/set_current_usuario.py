from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.domain.entities.usuario import Usuario


class SetCurrentUsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def execute(self, usuario: Usuario) -> None:
        self.repository.set_current_usuario(usuario)
