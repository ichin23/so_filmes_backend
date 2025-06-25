from abc import ABC, abstractmethod
from sofilmes.domain.entities.filme import Filme

class FilmesRepository(ABC):
    @abstractmethod
    def get_all(self)->list[Filme]:
        pass
    
    @abstractmethod
    def get_by_id(self, post_id: str)->Filme:
        pass

    @abstractmethod
    def create(self, filme: Filme)->None:
        pass

    @abstractmethod
    def update(self, filme: Filme)->None:
        pass