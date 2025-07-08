from sofilmes.domain.repositories.avaliacao_repositories import AvaliacaoRepository

class DeleteAvaliacaoUseCase:
    def __init__(self, repository: AvaliacaoRepository):
        self.repository = repository
    
    def execute(self, avaliacao_id:str)->bool:
        return self.repository.removerAvaliacao(avaliacao_id)