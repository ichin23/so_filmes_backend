from sofilmes.domain.repositories.avaliacao_repositories import AvaliacaoRepository

class SetAvaliacaoUseCase:
    def __init__(self, repository: AvaliacaoRepository):
        self.repository = repository

    def execute(self, avaliacao_id:str)-> None:
        return self.repository.set_avaliacao(avaliacao_id)