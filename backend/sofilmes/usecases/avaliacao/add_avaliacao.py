from sofilmes.domain.repositories.avaliacao_repositories import AvaliacaoRepository
from sofilmes.domain.entities.avaliacao import Avaliacao

class CreateAvalicaoUseCase:
    def __init__(self, repository: AvaliacaoRepository):
        self.repository = repository
    
    def execute(self, avaliacao:Avaliacao) -> Avaliacao:
        return self. repository.create(comment)