from sofilmes.domain.repositories.avaliacao_repositories import AvaliacaoRepository
from sofilmes.domain.entities.avaliacao import Avaliacao
from typing import List

class InMemoryCommentRepository(AvaliacaoRepository):
    def __init__(self):
        self._avaliacao = {}

    def get_avaliacao(self, id:str)->Avaliacao:
        for avaliacao in self._avaliacao.values():
            if avaliacao.id == id:
                return avaliacao
    
    def get_avaliacao_by_user(self, user_id:str)->List[Avaliacao]:
        avaliacoes = []
        for avaliacao in self._avaliacao.values():
            if avaliacao.user_id == user_id:
                avaliacoes.append(avaliacao)
        return avaliacoes
    
    def create(self, avaliacao:Avaliacao) -> None:
        self._avaliacao[avaliacao.id] = avaliacao
    
    def delete(self, id:str) -> None:
        if id in self._avaliacao:
            del self._avaliacao[id]
    
    def set_avaliacao(self, id:str, avaliacao:Avaliacao) -> None:
        if id not in self._avaliacao:
            raise ValueError(f"Avaliação com ID '{id}' não encontrada.")
        self._avaliacao[id] = avaliacao

