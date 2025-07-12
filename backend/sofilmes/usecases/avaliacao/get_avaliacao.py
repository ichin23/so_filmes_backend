from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import Optional


class GetAvaliacaoUseCase:
    def __init__(self, repository: AvaliacoesRepository):
        self.repository = repository

    async def execute(self, avaliacao_id: str) -> Optional[Avaliacao]:
        return await self.repository.getAvaliacao(avaliacao_id)
