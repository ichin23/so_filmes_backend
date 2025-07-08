from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository


class RemoverAvaliacao:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    def execute(self, avaliacao_id):
        return self._repo.removerAvaliacao(avaliacao_id)
