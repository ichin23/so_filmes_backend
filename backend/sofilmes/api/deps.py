from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sofilmes.domain.repositories.usuario_repositories import (
    UsuarioRepository as UserRepository,
)
from sofilmes.api.settings import settings
from sofilmes.domain.entities.usuario import Usuario
from sqlalchemy.ext.asyncio import AsyncSession
from collections.abc import AsyncGenerator
from sofilmes.infra.database import async_session
from sofilmes.infra.repositories.sqlalchemy.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from sofilmes.infra.repositories.sqlalchemy.sqlalchemy_filme_repository import (
    SQLAlchemyFilmeRepository,
)
from sofilmes.infra.repositories.sqlalchemy.sqlalchemy_avaliacao_repsoitory import (
    SQLAlchemyAvaliacaoRepository,
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_repository(
    db: AsyncSession = Depends(get_db_session),
) -> SQLAlchemyUserRepository:
    return SQLAlchemyUserRepository(db)


async def get_filmes_repository(
    db: AsyncSession = Depends(get_db_session),
) -> SQLAlchemyFilmeRepository:
    return SQLAlchemyFilmeRepository(db)


async def get_avaliacao_repository(
    db: AsyncSession = Depends(get_db_session),
) -> SQLAlchemyAvaliacaoRepository:
    return SQLAlchemyAvaliacaoRepository(db)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repo: UserRepository = Depends(get_user_repository),
) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        print("validade payload:")
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print(payload)
        user_id: str = str(payload.get("sub"))
        if user_id is None:
            raise credentials_exception
        user = await user_repo.get_by_id(user_id)
        if user is None:
            raise credentials_exception
        await user_repo.set_current_usuario(user)
    except JWTError:
        raise credentials_exception

    user = await user_repo.get_current_usuario()
    if user is None:
        raise credentials_exception
    return user
