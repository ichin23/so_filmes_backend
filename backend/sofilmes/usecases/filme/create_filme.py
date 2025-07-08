from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme


class CreateFilmeUseCase:
    def __init__(self, repository: FilmesRepository):
        self.repository = repository

    def execute(self, filme: Filme) -> Filme:
        return self.repository.create(filme)
