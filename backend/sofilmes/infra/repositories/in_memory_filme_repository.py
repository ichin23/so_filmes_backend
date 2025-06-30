from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme
from typing import List, Optional

class InMemoryFilmeRepository(FilmesRepository):
    def __init__(self):
        self._filmes = {}

    def get_all(self) -> List[Filme]:
        return list(self._filmes.values)
    
    def get_by_id(self, id) ->Optional[Filme]:
        return self._filmes.get(id)
    
    def create(self, filme):
        self._filmes[filme.id] = filme
        return filme

    def update(self, filme) -> Optional[Filme]:
        if filme.id in self._filmes:
            self._filmes[filme.id] = filme
            return filme
        return None

