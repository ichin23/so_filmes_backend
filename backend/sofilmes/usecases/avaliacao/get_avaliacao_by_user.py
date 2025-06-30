from sofilmes.domain.repositories.avaliacao_repositories import AvaliacaoRepository
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import List

class GetAvaliacaoByUserUseCase:
    def __init__(self, repository: AvaliacaoRepository):
        self.repository = repository

    def execute(self, user_id:str)-> List[Avaliacao]:
        return self.repository.get_avaliacao_by_user(user_id)