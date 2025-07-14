from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import Optional


class GetAvaliacoesByUsuarioEFilmeUseCase:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    async def execute(self, user_id, filme_id) -> Optional[Avaliacao]:
        return await self._repo.getAvaliacaoByUserEFilme(user_id, filme_id)
