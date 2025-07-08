from abc import ABC, abstractmethod
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import List, Optional

class AvaliacoesRepository(ABC):
    @abstractmethod
    def getAvaliacoesByFilme(self, filme_id:str)->List[Avaliacao]: ...

    @abstractmethod
    def getAvaliacoesByUser(self, user_id:str)->List[Avaliacao]: ...

    @abstractmethod
    def getAvaliacaoByUserEFilme(self, user_id: str, filme_id:str) -> Optional[Avaliacao]: ...

    @abstractmethod
    def criarAvaliacao(self, avaliacao: Avaliacao)-> Avaliacao: ...

    @abstractmethod
    def editarAvaliacao(self, avaliacao:Avaliacao) -> None: ...

    @abstractmethod
    def removerAvaliacao(self, avaliacao_id: str) -> None: ...


    