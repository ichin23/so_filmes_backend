from sofilmes.domain.repositories.filmes_repositories import FilmesRepository


class GetFilmesMaisAvaliados:
    def __init__(self, repo: FilmesRepository):
        self._repo = repo

    def execute(self):
        return self._repo.get_mais_avaliados()
