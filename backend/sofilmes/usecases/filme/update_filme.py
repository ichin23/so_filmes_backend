from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.domain.entities.filme import Filme
from typing import Optional

class UpdateFilmeUseCase:
    def __init__(self, repository: FilmesRepository):
        self._repository = repository

    def execute(self, filme:Filme) -> Optional[Filme]:
        return self._repository.update(filme)