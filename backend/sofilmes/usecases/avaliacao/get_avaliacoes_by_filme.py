from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository


class GetAvaliacoesByFilmeUseCase:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    async def execute(self, filme_id):
        return await self._repo.getAvaliacoesByFilme(filme_id)
