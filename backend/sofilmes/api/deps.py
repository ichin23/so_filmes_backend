from sofilmes.infra.repositories.in_memory_usuario_repository import (
    InMemoryUsuarioRepository,
)
from sofilmes.infra.repositories.in_memory_filme_repository import (
    InMemoryFilmeRepository,
)
from sofilmes.infra.repositories.in_memory_avaliacao_repository import (
    InMemoryAvaliacaoRepository,
)

# Instâncias em memória para simulação
user_repo = InMemoryUsuarioRepository()
filme_repo = InMemoryFilmeRepository()
avaliacao_repo_instance = InMemoryAvaliacaoRepository()


def avaliacao_repo():
    return avaliacao_repo_instance
