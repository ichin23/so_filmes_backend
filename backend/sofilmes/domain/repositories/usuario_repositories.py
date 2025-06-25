from abc import ABC, abstractmethod
from sofilmes.domain.entities.usuario import User

class UsuarioRepository(ABC):
    @abstractmethod
    def login(self, email:str, password:str)->User: 
        pass

    @abstractmethod
    def register(self, user:User)->None:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

    @abstractmethod
    def get_current_user(self)->User|None:
        pass

    @abstractmethod
    def set_current_user(self, user:User)->None:
        pass