from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from sofilmes.domain.entities.usuario import Usuario
from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password
from sofilmes.infra.models.user_model import UserModel

from sofilmes.infra.database import async_session


class SQLAlchemyUserRepository(UsuarioRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
        self._current_user: Optional[Usuario] = None

    async def register(self, user: Usuario) -> Usuario:
        try:
            model = UserModel.from_entity(user)
            self._session.add(model)
            await self._session.commit()
            await self._session.refresh(model)
            user.id = model.id
            return model.to_entity()
        except IntegrityError as e:
            print("username" in str(e._message))
            if "username" in str(e._message):
                raise ValueError("Nome de usuário já existente em outra conta")
            elif "email" in str(e._message):
                raise ValueError("Email já existente em outra conta")
            raise ValueError("Ocorreu um erro desconhecido")

    async def login(self, email: Email, password: Password) -> Optional[Usuario]:
        stmt = select(UserModel).where(UserModel.email == str(email))
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()

        if user and password.verify(user.senha):
            self._current_user = user.to_entity()
            print(self._current_user.media)
            return self._current_user
        return None

    async def set_current_user(self, user: Usuario) -> None:
        self._current_user = user

    async def logout(self) -> None:
        self._current_user = None

    async def get_by_email(self, email: Email) -> Optional[Usuario]:
        stmt = select(UserModel).where(UserModel.email == str(email))
        result = await self._session.execute(stmt)
        user_model = result.scalar_one_or_none()
        return user_model.to_entity() if user_model else None

    async def get_by_id(self, id: str) -> Optional[Usuario]:
        stmt = select(UserModel).where(UserModel.id == str(id))
        result = await self._session.execute(stmt)
        user_model = result.scalar_one_or_none()
        return user_model.to_entity() if user_model else None

    async def get_current_usuario(self) -> Optional[Usuario]:
        if self._current_user is None:
            raise ValueError("Current user is not set. Please log in first.")
        stmt = select(UserModel).where(UserModel.id == str(self._current_user.id))
        result = await self._session.execute(stmt)
        user = result.unique().scalar_one_or_none()
        if user:
            self._current_user = user.to_entity()
        else:
            self._current_user = None
        return self._current_user

    async def set_current_usuario(self, user: Usuario) -> None:
        self._current_user = user
