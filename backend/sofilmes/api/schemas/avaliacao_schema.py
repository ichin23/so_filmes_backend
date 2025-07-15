from pydantic import BaseModel, Field
from typing import Optional, TYPE_CHECKING
from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.api.schemas.filme_schema import FilmeOutput

from sofilmes.api.schemas.user_schema import UserOutput


class CreateAvaliacaoInput(BaseModel):
    filme_id: str = Field(..., description="ID do filme avaliado")
    # user_id: str = Field(..., description="ID do usuário que fez a avaliação")
    comentario: str = Field(
        ..., min_length=1, max_length=500, description="Comentario da avaliação"
    )
    avaliacao: float = Field(..., ge=1, le=5, description="Nota do Filme")


class AvaliacaoFilmeEUserInput(BaseModel):
    filme_id: str = Field(..., description="ID do filme avaliado")
    user_id: str = Field(..., description="ID do usuário que fez a avaliação")


class AvaliacaoOutput(BaseModel):
    id: str = Field(..., description="ID do post")
    comentario: str
    avaliacao: float
    user_id: str
    filme_id: str
    user: UserOutput = Field(..., description="Dados do usuário que está postando")
    filme: FilmeOutput = Field(..., description="Dados do filme que está sendo postado")

    @classmethod
    def from_entity(cls, avaliacao):
        return cls(
            id=avaliacao.id,
            filme=avaliacao.filme,
            user_id=avaliacao.user,
            comentario=avaliacao.comentario,
            avaliacao=avaliacao.avaliacao,
        )


def avaliacao_to_output(avaliacao: Avaliacao) -> AvaliacaoOutput:
    return AvaliacaoOutput(
        id=avaliacao.id,
        filme=FilmeOutput.from_entity(avaliacao.filme),
        user=UserOutput.from_entity(avaliacao.user),
        user_id=avaliacao.user_id,
        filme_id=avaliacao.filme_id,
        avaliacao=avaliacao.avaliacao,
        comentario=avaliacao.comentario,
    )


def avaliacoes_to_output(avaliacoes: list[Avaliacao]) -> list[AvaliacaoOutput]:
    return [avaliacao_to_output(avaliacao) for avaliacao in avaliacoes]
