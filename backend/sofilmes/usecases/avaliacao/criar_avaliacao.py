from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository

class CriarAvaliacaoUseCase:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    def execute(self, avaliacao):
        return self._repo.criarAvaliacao(avaliacao)