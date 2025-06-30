from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme

class UpdateFilmeUseCase:
    def __init__(self, repository: FilmesRepository):
        self._repository = repository

    def execute(self, filme:Filme) -> Filme:
        return self._repository.update(filme)