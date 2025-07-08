from abc import ABC, abstractmethod
from sofilmes.domain.entities.filme import Filme
from typing import Optional


class FilmesRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Filme]:
        pass

    @abstractmethod
    def get_by_id(self, post_id: str) -> Optional[Filme]:
        pass

    @abstractmethod
    def create(self, filme: Filme) -> Filme:
        pass

    @abstractmethod
    def update(self, filme: Filme) -> Optional[Filme]:
        pass
