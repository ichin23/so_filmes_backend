from sofilmes.domain.entities.avaliacao import Avaliacao
import uuid
from sofilmes.infra.repositories.in_memory_avaliacao_repository import InMemoryAvaliacaoRepository
from sofilmes.usecases.avaliacao.criar_avaliacao import CriarAvaliacaoUseCase
from sofilmes.usecases.avaliacao.get_avaliacoes_by_filme import GetAvaliacoesByFilmeUseCase
from sofilmes.usecases.avaliacao.get_avaliacoes_by_usuario import GetAvaliacoesByUsuarioUseCase

def create_test_avaliacao(user_id=None, filme_id=None):
    return Avaliacao(
        id=str(uuid.uuid4()),
        autor_id=user_id or str(uuid.uuid4()),
        filme_id=filme_id or str(uuid.uuid4()),
        avaliacao=5,
        comentario="Muito bom"
    )

def test_create_avaliacao():
    repo = InMemoryAvaliacaoRepository()
    avaliacao = create_test_avaliacao()

    usecase = CriarAvaliacaoUseCase(repo)
    result = usecase.execute(avaliacao)

    assert result == avaliacao
    assert repo._avaliacoes[avaliacao.id] == avaliacao

def test_get_avaliacoes_by_filme():
    repo = InMemoryAvaliacaoRepository()
    filme_id = str(uuid.uuid4())
    avaliacao = create_test_avaliacao(filme_id=filme_id)
    avaliacao2 = create_test_avaliacao(filme_id=filme_id)
    avaliacao3 = create_test_avaliacao()

    repo.criarAvaliacao(avaliacao)
    repo.criarAvaliacao(avaliacao2)
    repo.criarAvaliacao(avaliacao3)

    usecase = GetAvaliacoesByFilmeUseCase(repo)
    result = usecase.execute(filme_id)

    assert avaliacao in result
    assert avaliacao2 in result
    assert avaliacao3 not in result
    assert len(result) == 2

def test_get_avaliacaoes_by_user():
    repo = InMemoryAvaliacaoRepository()
    user_id = str(uuid.uuid4())
    avaliacao = create_test_avaliacao(user_id=user_id)
    avaliacao2 = create_test_avaliacao(user_id=user_id)
    avaliacao3 = create_test_avaliacao()

    repo.criarAvaliacao(avaliacao)
    repo.criarAvaliacao(avaliacao2)
    repo.criarAvaliacao(avaliacao3)

    usecase = GetAvaliacoesByUsuarioUseCase(repo)
    result = usecase.execute(user_id)

    assert avaliacao in result
    assert avaliacao2 in result
    assert avaliacao3 not in result
    assert len(result) == 2

def test_get_avaliacaoes_by_filme_empty():
    repo = InMemoryAvaliacaoRepository()
    usecase = GetAvaliacoesByFilmeUseCase(repo)
    result = usecase.execute("filme-1")

    assert result == []





    
