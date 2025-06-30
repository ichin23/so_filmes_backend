from abc import ABC, abstractmethod
from sofilmes.domain.entities.usuario import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    def login(self, email:str, password:str)->Usuario: 
        pass

    @abstractmethod
    def register(self, usuario:Usuario)->None:
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