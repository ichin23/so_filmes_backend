from sofilmes.domain.repositories.filmes_repositories import FilmesRepository


class GetAllFilmeUseCase:
    def __init__(self, repository: FilmesRepository):
        self.repository = repository

    async def execute(self):
        return await self.repository.get_all()
