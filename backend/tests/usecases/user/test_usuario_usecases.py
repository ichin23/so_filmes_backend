import pytest
import uuid
from sofilmes.domain.entities.usuario import Usuario
from sofilmes.domain.value_objects.senha_vo import Password
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.infra.repositories.in_memory.in_memory_usuario_repository import (
    InMemoryUsuarioRepository,
)
from sofilmes.usecases.usuario.register_usuario import RegisterUsuarioUseCase
from sofilmes.usecases.usuario.login_usuario import LoginUsuarioUseCase
from sofilmes.usecases.usuario.logout_usuario import LogoutUsuarioUseCase
from sofilmes.usecases.usuario.get_current_usuario import GetCurrentUsuarioUseCase
from sofilmes.usecases.usuario.set_current_usuario import SetCurrentUsuarioUseCase


def create_test_usuario() -> Usuario:
    return Usuario(
        id=str(uuid.uuid4()),
        nome="Test Usuario",
        email=Email("test@example.com"),
        senha=Password("secur3Pass@"),
        username="usuario",
    )

@pytest.mark.asyncio
async def test_register_usuario():
    repo = InMemoryUsuarioRepository()
    usecase = RegisterUsuarioUseCase(repo)
    usuario = create_test_usuario()

    result = await usecase.execute(usuario)

    assert result == usuario
    assert await repo.get_current_usuario() == usuario


@pytest.mark.asyncio
async def test_login_usuario_success():
    repo = InMemoryUsuarioRepository()
    usuario = create_test_usuario()
    repo.register(usuario)

    usecase = LoginUsuarioUseCase(repo)
    result = await  usecase.execute(usuario.email, usuario.senha)

    assert result == usuario
    assert await repo.get_current_usuario() == usuario


@pytest.mark.asyncio
async def test_login_usuario_failure():
    repo = InMemoryUsuarioRepository()
    usecase = LoginUsuarioUseCase(repo)
    email = Email("notfound@example.com")
    senha = Password("wrongP1ss@")

    result = await  usecase.execute(email, senha)

    assert result is None
    assert await repo.get_current_usuario() is None


@pytest.mark.asyncio
async def test_logout_usuario():
    repo = InMemoryUsuarioRepository()
    usuario = create_test_usuario()
    repo.register(usuario)
    repo.login(usuario.email, usuario.senha)

    usecase = LogoutUsuarioUseCase(repo)
    await usecase.execute()

    assert await repo.get_current_usuario() is None


@pytest.mark.asyncio
async def test_get_current_usuario():
    repo = InMemoryUsuarioRepository()
    usuario = create_test_usuario()
    repo.register(usuario)

    usecase = GetCurrentUsuarioUseCase(repo)
    result = await usecase.execute()

    assert result == usuario


@pytest.mark.asyncio
async def test_set_current_usuario():
    repo = InMemoryUsuarioRepository()
    usuario = create_test_usuario()

    usecase = SetCurrentUsuarioUseCase(repo)
    await usecase.execute(usuario)

    assert await repo.get_current_usuario() == usuario
