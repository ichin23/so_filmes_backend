from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme
from typing import Optional


class GetByIdFilmeUseCase:
    def __init__(self, repository: FilmesRepository):
        self.repository = repository

    async def execute(self, id: str) -> Optional[Filme]:
        return await self.repository.get_by_id(id)
