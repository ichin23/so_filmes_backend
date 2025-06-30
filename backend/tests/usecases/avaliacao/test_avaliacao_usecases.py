import uuid
from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.infra.repositories.in_memory_avaliacao_repository import Avaliacao
from sofilmes.usecases.avaliacao.add_avaliacao import CreateAvalicaoUseCase
from sofilmes.usecases.avaliacao.delete_avaliacao import DeleteAvaliacaoUseCase
from sofilmes.usecases.avaliacao.get_avaliacao import GetAvaliacaoUseCase
from sofilmes.usecases.avaliacao.get_avaliacao_by_user import GetAvaliacaoByUserUseCase
from sofilmes.usecases.avaliacao.set_avaliacao import SetAvaliacaoUseCase

def create_test_avaliacao(user_id=None, post_id=None) -> Avaliacao:
    return Avaliacao(
        id=str(uuid.uuid4()),
        user_id=user_id or str(uuid.uuid4()),
        quant = 5,
        comentario="testando"
    )
    
