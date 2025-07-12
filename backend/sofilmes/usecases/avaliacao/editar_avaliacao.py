from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository


class EditarAvaliacaoUseCase:
    def __init__(self, repo: AvaliacoesRepository):
        self._repo = repo

    async def execute(self, avaliacao):
        return await self._repo.editarAvaliacao(avaliacao)
