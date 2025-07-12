from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import List


class GetUltimasAvaliacoesUseCase:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    async def execute(self) -> List[Avaliacao]:
        return await self._repo.getUltimasAvaliacoes()
