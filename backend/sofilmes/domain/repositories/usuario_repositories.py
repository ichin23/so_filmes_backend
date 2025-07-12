from abc import ABC, abstractmethod
from sofilmes.domain.entities.usuario import Usuario
from typing import Optional
from sofilmes.domain.value_objects.senha_vo import Password
from sofilmes.domain.value_objects.email_vo import Email


class UsuarioRepository(ABC):
    @abstractmethod
    async def login(self, email: Email, password: Password) -> Optional[Usuario]:
        pass

    @abstractmethod
    async def register(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    async def logout(self) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> Optional[Usuario]:
        pass

    @abstractmethod
    async def get_current_usuario(self) -> Usuario | None:
        pass

    @abstractmethod
    async def set_current_usuario(self, usuario: Usuario) -> None:
        pass
