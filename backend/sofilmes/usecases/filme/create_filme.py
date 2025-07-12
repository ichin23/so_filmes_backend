from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme


class CreateFilmeUseCase:
    def __init__(self, repository: FilmesRepository):
        self.repository = repository

    async def execute(self, filme: Filme) -> Filme:
        return await self.repository.create(filme)
