from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.domain.entities.usuario import Usuario
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password
from typing import Optional


class InMemoryUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self._usuarios = {}
        self._current_usuario_id = None

    def register(self, usuario: Usuario) -> Optional[Usuario]:
        self._usuarios[usuario.id] = usuario
        self._current_usuario_id = usuario.id
        return usuario

    def login(self, email: Email, password: Password) -> Optional[Usuario]:
        for usuario in self._usuarios.values():
            
            if usuario.email == email and usuario.senha == password:
                self._current_usuario_id = usuario.id
                return usuario
        return None

    def logout(self) -> None:
        self._current_usuario_id = None

    def get_current_usuario(self) -> Optional[Usuario]:
        if self._current_usuario_id is None:
            return None
        return self._usuarios.get(self._current_usuario_id)

    def set_current_usuario(self, usuario: Usuario) -> None:
        self._usuarios[usuario.id] = usuario
        self._current_usuario_id = usuario.id