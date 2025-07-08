from sofilmes.api.schemas.user_schema import (
    LoginUserInput,
    RegisterUserInput,
    RegisterUserResponse,
    UserOutput,
)
from sofilmes.domain.entities.usuario import Usuario
import uuid
from fastapi import APIRouter, HTTPException
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password
from sofilmes.usecases.usuario.register_usuario import RegisterUsuarioUseCase
from sofilmes.api.deps import user_repo
from sofilmes.usecases.usuario.login_usuario import LoginUsuarioUseCase
from sofilmes.usecases.usuario.logout_usuario import LogoutUsuarioUseCase
from sofilmes.usecases.usuario.get_current_usuario import GetCurrentUsuarioUseCase


router = APIRouter()


@router.post(
    "/register",
    response_model=RegisterUserResponse,
    summary="Registrar novo usuário",
    description="Cria um novo usuário com nome, email e senha forte.",
)
def register_usuario(data: RegisterUserInput):
    try:
        user = Usuario(
            id=str(uuid.uuid4()),
            nome=data.nome,
            username=data.username,
            email=Email(str(data.email)),
            senha=Password(data.password),
        )

        usecase = RegisterUsuarioUseCase(user_repo)
        result = usecase.execute(user)

        if result is None:
            raise HTTPException(status_code=404, detail="Erro no usuário")

        return RegisterUserResponse(
            message="User Registered Successfully",
            user=UserOutput(
                id=result.id,
                nome=result.nome,
                email=str(result.email),
                username=result.username,
            ),
        )
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/login",
    response_model=UserOutput,
    summary="Fazer o Login do usuário",
    description="Autentica um usuário com email e senha forte.",
)
def login_user(data: LoginUserInput):
    try:

        usecase = LoginUsuarioUseCase(user_repo)
        result = usecase.execute(Email(data.email), Password(data.password))

        if result is None:
            raise HTTPException(status_code=404, detail="Usuário not found")

        return UserOutput(
            id=result.id,
            nome=result.nome,
            email=str(result.email),
            username=result.username,
        )

    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post(
    "/logout",
    summary="Fazer o Logout do usuário",
    description="Descredencia o usuário autenticado.",
)
def logout_user():
    usecase = LogoutUsuarioUseCase(user_repo)
    usecase.execute()

    return {"message": "Logout succesful"}


@router.get(
    "/me",
    response_model=UserOutput,
    summary="Informar os dados do usuário atual",
    description="Retorna os dados do usuário atual.",
)
def get_current_user():
    try:
        usecase = GetCurrentUsuarioUseCase(user_repo)
        result = usecase.execute()
        return {
            "id": result.id,
            "nome": result.nome,
            "username": result.username,
            "email": str(result.email),
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
