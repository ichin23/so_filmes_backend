from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from typing import List

class InMemoryAvaliacaoRepository(AvaliacoesRepository):
    def __init__(self):
        self._avaliacoes = {}
    
    def getAvaliacaoByUserEFilme(self, user_id, filme_id)->List[Avaliacao]:
        avaliacoes = []
        for avaliacao in self._avaliacoes.values():
            if avaliacao.autor_id == user_id and avaliacao.filme_id == filme_id:
                avaliacoes.append(avaliacao)
        return avaliacoes
    
    def getAvaliacoesByFilme(self, filme_id)->List[Avaliacao]:
        avaliacoes = []
        for avaliacao in self._avaliacoes.values():
            if avaliacao.filme_id == filme_id:
                avaliacoes.append(avaliacao)
        return avaliacoes
    
    def getAvaliacoesByUser(self, user_id) -> List[Avaliacao]:
        avaliacoes = []
        for avaliacao in self._avaliacoes.values():
            if avaliacao.autor_id == user_id:
                avaliacoes.append(avaliacao)
        return avaliacoes
    
    def criarAvaliacao(self, avaliacao: Avaliacao)->Avaliacao:
        self._avaliacoes[avaliacao.id] = avaliacao
        return avaliacao
    
    def editarAvaliacao(self, avaliacao:Avaliacao)->None:
        self._avaliacoes[avaliacao.id] = avaliacao

    def removerAvaliacao(self, avaliacao_id)->None:
        del self._avaliacoes[avaliacao_id]
        return None
