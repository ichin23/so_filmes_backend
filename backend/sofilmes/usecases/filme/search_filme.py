from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme


class SearchFilmeUseCase:
    def __init__(self, repo: FilmesRepository):
        self._repo = repo

    async def execute(self, filmeQuery: str) -> list[Filme]:
        return await self._repo.search_filme(filmeQuery)
