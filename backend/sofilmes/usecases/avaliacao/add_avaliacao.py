from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.domain.entities.avaliacao import Avaliacao

class CreateAvalicaoUseCase:
    def __init__(self, repository: AvaliacoesRepository):
        self.repository = repository
    
    def execute(self, avaliacao:Avaliacao) -> Avaliacao:
        return self.repository.criarAvaliacao(avaliacao)
