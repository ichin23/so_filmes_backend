from abc import ABC, abstractmethod
from sofilmes.domain.entities.usuario import Usuario
from typing import Optional
from sofilmes.domain.value_objects.senha_vo import Password
from sofilmes.domain.value_objects.email_vo import Email

class UsuarioRepository(ABC):
    @abstractmethod
    def login(self, email:Email, password:Password)->Optional[Usuario]: 
        pass

    @abstractmethod
    def register(self, usuario:Usuario)->Optional[Usuario]:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

    @abstractmethod
    def get_current_usuario(self)->Usuario|None:
        pass

    @abstractmethod
    def set_current_usuario(self, usuario:Usuario)->None:
        pass