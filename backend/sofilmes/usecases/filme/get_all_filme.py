from sofilmes.domain.repositories.filmes_repositories import FilmesRepository

class GetAllFilmeUseCase:
    def __init__(self, repository: FilmesRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()