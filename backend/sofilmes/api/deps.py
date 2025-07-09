from sofilmes.infra.repositories.in_memory_usuario_repository import (
    InMemoryUsuarioRepository,
)
from sofilmes.infra.repositories.in_memory_filme_repository import (
    InMemoryFilmeRepository,
)
from sofilmes.infra.repositories.in_memory_avaliacao_repository import (
    InMemoryAvaliacaoRepository,
)

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sofilmes.infra.database import async_session


# Instâncias em memória para simulação
user_repo = InMemoryUsuarioRepository()
filme_repo = InMemoryFilmeRepository()
avaliacao_repo_instance = InMemoryAvaliacaoRepository()

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


def avaliacao_repo():
    return avaliacao_repo_instance
