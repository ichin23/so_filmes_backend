import pytest
from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme
from typing import List, Optional


class InMemoryFilmeRepository(FilmesRepository):
    def __init__(self):
        self._filmes = {}

    @pytest.mark.asyncio
    async def get_all(self) -> List[Filme]:
        return list(self._filmes.values())

    @pytest.mark.asyncio
    async def get_ultimos_filmes(self):
        return list(self._filmes.values()).sort(lambda filme: filme.ano)

    @pytest.mark.asyncio
    async def get_by_id(self, id) -> Optional[Filme]:
        return self._filmes.get(id)

    @pytest.mark.asyncio
    async def get_mais_avaliados(self):
        return self._filmes

    @pytest.mark.asyncio
    async def create(self, filme):
        self._filmes[filme.id] = filme
        return filme

    @pytest.mark.asyncio
    async def update(self, filme) -> Optional[Filme]:
        if filme.id in self._filmes:
            self._filmes[filme.id] = filme
            return filme
        return None
