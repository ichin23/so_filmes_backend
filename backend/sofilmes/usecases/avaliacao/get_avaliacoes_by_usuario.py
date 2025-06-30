from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository

class GetAvaliacoesByUsuarioUseCase:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    def execute(self, user_id):
        return self._repo.getAvaliacoesByUser(user_id)