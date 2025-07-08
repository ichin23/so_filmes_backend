from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository


class DeleteAvaliacaoUseCase:
    def __init__(self, repository: AvaliacoesRepository):
        self.repository = repository

    def execute(self, avaliacao_id: str) -> bool:
        return self.repository.removerAvaliacao(avaliacao_id)
