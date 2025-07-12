from abc import ABC, abstractmethod
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import List, Optional


class AvaliacoesRepository(ABC):
    @abstractmethod
    async def getAvaliacoesByFilme(self, filme_id: str) -> List[Avaliacao]: ...

    @abstractmethod
    async def getAvaliacao(self, avaliacao_id) -> Optional[Avaliacao]: ...

    @abstractmethod
    async def getUltimasAvaliacoes(self) -> List[Avaliacao]: ...

    @abstractmethod
    async def getAvaliacoesByUser(self, user_id: str) -> List[Avaliacao]: ...

    @abstractmethod
    async def getAvaliacaoByUserEFilme(
        self, user_id: str, filme_id: str
    ) -> Optional[Avaliacao]: ...

    @abstractmethod
    async def criarAvaliacao(self, avaliacao: Avaliacao) -> Avaliacao: ...

    @abstractmethod
    async def editarAvaliacao(self, avaliacao: Avaliacao) -> Optional[Avaliacao]: ...

    @abstractmethod
    async def removerAvaliacao(self, avaliacao_id: str) -> bool: ...
