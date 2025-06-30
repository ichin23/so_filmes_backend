from abc import ABC, abstractmethod
from sofilmes.domain.entities.avaliacao import Avaliacao

class AvaliacaoRepository(ABC):

    @abstractmethod
    def create(self, avaliacao:Avaliacao) -> None:
        pass

    @abstractmethod
    def delete(self, id:str) -> None:
        pass

    @abstractmethod
    def set_avaliacao(self, id:str) -> None:
        pass
    
    @abstractmethod
    def get_avaliacao(self, id:str) -> Avaliacao:
        pass
    
    @abstractmethod
    def get_avaliacao_by_user(self, user_id:str)->list[Avaliacao]:
        pass