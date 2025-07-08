from pydantic import BaseModel, Field
from typing import Optional

class CreateAvaliacaoInput(BaseModel):
    filme_id:str = Field(..., description="ID do filme avaliado")
    user_id:str = Field(..., description="ID do usuário que fez a avaliação")
    comentario:str = Field(..., min_length=1, max_length=500, description="Comentario da avaliação")
    avaliacao:float = Field(..., ge=1, le=5, description="Nota do Filme")

class AvaliacaoOutput(BaseModel):
    id: str
    filme_id: str
    user_id: str
    comentario: str
    avaliacao: float


    @classmethod
    def from_entity(cls, avaliacao):
        return cls(
            id=avaliacao.id,
            filme_id=avaliacao.filme_id,
            user_id=avaliacao.user_id,
            comentario=avaliacao.comentario,
            avaliacao=avaliacao.avaliacao,
        )
