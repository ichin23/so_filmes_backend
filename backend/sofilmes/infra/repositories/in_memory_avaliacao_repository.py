from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from typing import List

class InMemoryAvaliacaoRepository(AvaliacoesRepository):
    def __init__(self):
        self._avaliacoes = {}
    
    def getAvaliacaoByUserEFilme(self, user_id, filme_id)->List[Avaliacao]:
        avaliacoes = []
        for avaliacao in self._avaliacoes.values():
            if avaliacao.user_id == user_id and avaliacao.filme_id == filme_id:
                avaliacoes.append(avaliacao)
        return avaliacoes
    
    def getAvaliacoesByFilme(self, filme_id)->List[Avaliacao]:
        avaliacoes = []
        for avaliacao in self._avaliacoes.values():
            if avaliacao.filme_id == filme_id:
                avaliacoes.append(avaliacao)
        return avaliacoes
    
    def getAvaliacao(self, avaliacao_id)->Avaliacao:
        for avaliacao in self._avaliacoes.values():
            if avaliacao.id == avaliacao_id:
                return avaliacao
        return None
            
    
    def getAvaliacoesByUser(self, user_id) -> List[Avaliacao]:
        avaliacoes = []
        for avaliacao in self._avaliacoes.values():
            if avaliacao.user_id == user_id:
                avaliacoes.append(avaliacao)
        return avaliacoes
    
    def criarAvaliacao(self, avaliacao: Avaliacao)->Avaliacao:
        self._avaliacoes[avaliacao.id] = avaliacao
        return avaliacao
    
    def editarAvaliacao(self, avaliacao:Avaliacao) -> Avaliacao:
        if avaliacao.id in self._avaliacoes:
            self._avaliacoes[avaliacao.id] = avaliacao
            return avaliacao
        return None

    def removerAvaliacao(self, avaliacao_id: str) -> bool:
        if avaliacao_id in self._avaliacoes:
            del self._avaliacoes[avaliacao_id]
            return True
        return False

