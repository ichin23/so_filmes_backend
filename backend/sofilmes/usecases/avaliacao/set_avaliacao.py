from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import Optional


class SetAvaliacaoUseCase:
    def __init__(self, repository: AvaliacoesRepository):
        self.repository = repository

    def execute(self, avaliacao: Avaliacao) -> Optional[Avaliacao]:
        return self.repository.editarAvaliacao(avaliacao)
