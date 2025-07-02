from sofilmes.infra.repositories.in_memory_usuario_repository import InMemoryUsuarioRepository
from sofilmes.infra.repositories.in_memory_filme_repository import InMemoryFilmeRepository
from sofilmes.infra.repositories.in_memory_avaliacao_repository import InMemoryAvaliacaoRepository

# Instâncias em memória para simulação
user_repo = InMemoryUsuarioRepository()
post_repo = InMemoryFilmeRepository()
comment_repo = InMemoryAvaliacaoRepository()