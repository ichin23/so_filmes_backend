from sofilmes.api.schemas.user_schema import (
    LoginUserInput,
    RegisterUserInput,
    RegisterUserResponse,
    TokenResponse,
    user_to_output,
    UserOutput,
)
from sofilmes.domain.entities.usuario import Usuario
from sqlalchemy.ext.asyncio import AsyncSession
from sofilmes.api.deps import get_db_session, get_user_repository, get_current_user
import uuid
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password, PasswordValidationError
from sofilmes.usecases.usuario.register_usuario import RegisterUsuarioUseCase
from sofilmes.usecases.usuario.login_usuario import LoginUsuarioUseCase
from sofilmes.usecases.usuario.logout_usuario import LogoutUsuarioUseCase
from sofilmes.usecases.usuario.get_current_usuario import GetCurrentUsuarioUseCase
from sofilmes.infra.repositories.sqlalchemy.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from sofilmes.domain.repositories.usuario_repositories import UsuarioRepository
from sofilmes.api.security import create_access_token

security = HTTPBearer()
router = APIRouter()


@router.post(
    "/register",
    response_model=RegisterUserResponse,
    summary="Registrar novo usuário",
    description="Cria um novo usuário com nome, email e senha forte.",
    
)
async def register_usuario(
    data: RegisterUserInput, db: AsyncSession = Depends(get_db_session)
):
    try:
        user_repo = SQLAlchemyUserRepository(db)
        user = Usuario(
            id=str(uuid.uuid4()),
            nome=data.nome,
            username=data.username,
            email=Email(str(data.email)),
            senha=Password(data.password)
        )

        usecase = RegisterUsuarioUseCase(user_repo)
        result = await usecase.execute(user)

        return RegisterUserResponse(
            message="User Registered Successfully",
            user=UserOutput(
                id=result.id,
                nome=result.nome,
                email=str(result.email),
                username=result.username,
            ),
        )
    except PasswordValidationError as p:
        raise HTTPException(status_code=400, detail=str(p))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Fazer o Login do usuário",
    description="Autentica um usuário com email e senha forte.",
)
async def login_user(
    data: LoginUserInput,
    user_repo: UsuarioRepository = Depends(get_user_repository),
):
    try:

        usecase = LoginUsuarioUseCase(user_repo)
        result = await usecase.execute(Email(data.email), Password(data.password))
        print(result)
        if not result:
            raise HTTPException(status_code=404, detail="Usuário not found")

        token = create_access_token(data={"sub": str(result.id)})
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            user=user_to_output(result),
        )

    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get(
    "/me",
    response_model=UserOutput,
    summary="Informar os dados do usuário atual",
    description="Retorna os dados do usuário atual.",
)
async def get_me_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user: Usuario = Depends(get_current_user),
):
    try:
        return {
            "id": user.id,
            "nome": user.nome,
            "username": user.username,
            "email": str(user.email),
            "media": user.media
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
