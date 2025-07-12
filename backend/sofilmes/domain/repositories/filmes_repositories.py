from abc import ABC, abstractmethod
from sofilmes.domain.entities.filme import Filme
from typing import Optional


class FilmesRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Filme]:
        pass

    @abstractmethod
    async def get_mais_avaliados(self) -> list[Filme]:
        pass

    @abstractmethod
    async def get_by_id(self, post_id: str) -> Optional[Filme]:
        pass

    @abstractmethod
    async def create(self, filme: Filme) -> Filme:
        pass
