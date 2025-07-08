from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import List


class GetAvaliacaoByUserUseCase:
    def __init__(self, repository: AvaliacoesRepository):
        self.repository = repository

    def execute(self, user_id: str) -> List[Avaliacao]:
        return self.repository.getAvaliacoesByUser(user_id)
