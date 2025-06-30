from abc import ABC, abstractmethod
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import List, Optional

class AvaliacoesRepository(ABC):
    @abstractmethod
    def getAvaliacoesByFilme()->List[Avaliacao]: ...

    @abstractmethod
    def getAvaliacoesByUser(user_id:str)->List[Avaliacao]: ...

    @abstractmethod
    def getAvaliacaoByUserEFilme(user_id: str, filme_id:str) -> Optional[Avaliacao]: ...

    @abstractmethod
    def criarAvaliacao(avaliacao: Avaliacao)-> Avaliacao: ...

    @abstractmethod
    def editarAvaliacao(avaliacao:Avaliacao) -> None: ...

    @abstractmethod
    def removerAvaliacao(avaliacao_id: str) -> None: ...


    