from pydantic import BaseModel, EmailStr, Field
from typing import List, TYPE_CHECKING
from sofilmes.domain.entities.usuario import Usuario


class RegisterUserInput(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50, description="Nome do usuário")
    username: str = Field(
        ..., min_length=3, max_length=20, description="Regsitro de usuário"
    )
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=8, description="Senha do usuário")
    # role: Literal["user", "admin"]


class LoginUserInput(BaseModel):
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=8, description="Senha do usuário")


class SetCurrentUserInput(BaseModel):
    user_id: str = Field(..., description="ID do usuário a ser definido como atual")


class UserOutput(BaseModel):
    id: str = Field(..., description="ID do usuário")
    nome: str = Field(..., min_length=3, max_length=50, description="Nome do usuário")
    username: str = Field(
        ..., min_length=3, max_length=20, description="Regsitro de usuário"
    )
    email: str = Field(..., description="Email do usuário")
    media: float = Field(..., description="Média de avaliações do usuário")
    # role: str = Field(..., description="Papel do usuário (admin, user)")

    @classmethod
    def from_entity(cls, user):
        return cls(
            id=user.id,
            nome=user.nome,
            username=user.username,
            email=str(user.email),
            media=user.media
            # role=user.role,
        )


class RegisterUserResponse(BaseModel):
    message: str
    user: UserOutput


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserOutput


def user_to_output(user: Usuario) -> UserOutput:
    return UserOutput(
        id=user.id,
        nome=user.nome,
        username=user.username,
        email=str(user.email),
        media=user.media
    )
