from abc import ABC, abstractmethod
from sofilmes.domain.entities.avaliacao import Avaliacao

class AvaliacaoRepository(ABC):
    @abstractmethod
    def get_all(self)->list[Avaliacao]:
        pass
    
    @abstractmethod
    def create(self, avaliacao:Avaliacao):
        pass

    @abstractmethod
    def delete(self, id:str):
        pass

    @abstractmethod
    def set_avaliacao(self, id:str):
        pass
    
    @abstractmethod
    def get_avaliacao(self, id:str):
        pass