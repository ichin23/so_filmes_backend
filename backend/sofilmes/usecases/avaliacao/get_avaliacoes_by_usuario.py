from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository


class GetAvaliacoesByUsuarioUseCase:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    async def execute(self, user_id):
        return await self._repo.getAvaliacoesByUser(user_id)
