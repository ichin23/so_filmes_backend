import uuid
from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.infra.repositories.in_memory_avaliacao_repository import Avaliacao
from sofilmes.usecases.avaliacao.add_avaliacao import CreateAvalicaoUseCase
from sofilmes.usecases.avaliacao.delete_avaliacao import DeleteAvaliacaoUseCase
from sofilmes.usecases.avaliacao.get_avaliacao import GetAvaliacaoUseCase
from sofilmes.usecases.avaliacao.get_avaliacao_by_user import GetAvaliacaoByUserUseCase
from sofilmes.usecases.avaliacao.set_avaliacao import SetAvaliacaoUseCase
from sofilmes.infra.repositories.in_memory_avaliacao_repository import InMemoryAvaliacaoRepository

def create_test_avaliacao(user_id=None, post_id=None) -> Avaliacao:
    return Avaliacao(
        id=str(uuid.uuid4()),
        user_id=user_id or str(uuid.uuid4()),
        quant = 5,
        comentario="testando"
    )

def test_get_avaliacao_by_user_id():
    repo = InMemoryAvaliacaoRepository()
    user_id = str(uuid.uuid4())
    avaliacao1 = create_test_avaliacao(user_id=user_id)
    avaliacao2 = create_test_avaliacao(user_id=user_id)

    avaliacao3 = create_test_avaliacao()

    repo.create(avaliacao1)
    repo.create(avaliacao2)
    repo.create(avaliacao3)

    usecase = GetAvaliacaoByUserUseCase(repo)
    result = usecase.execute(user_id)

    assert avaliacao1 in result
    assert avaliacao2 in result
    assert avaliacao3 not in result
    assert len(result) == 2

def test_get_avaliacao():
    repo = InMemoryAvaliacaoRepository()
    avaliacao1 = create_test_avaliacao("10")
    repo.create(avaliacao1)

    usecase = GetAvaliacaoUseCase(repo)
    result = usecase.execute(avaliacao1.id)

    assert avaliacao1.id == result.id


    
