from pydantic import BaseModel, Field
from typing import List

class FilmeInput(BaseModel):
    titulo: str = Field(..., description="Título do filme")
    tituloOriginal: str = Field(..., description="Título original do filme")
    capa: str = Field(..., description="URL ou caminho da imagem da capa")
    descricao: str = Field(..., min_length=10, max_length=1000, description="Descrição do filme")
    avaliacao: float = Field(..., ge=0, le=10, description="Nota média do filme (0 a 10)")
    ano: int = Field(..., ge=1800, le=2100, description="Ano de lançamento do filme")
    generos: List[str] = Field(..., description="Lista de gêneros do filme")
    diretor: str = Field(..., description="Nome do diretor do filme")

class FilmeOutput(BaseModel):
    id: str = Field(..., description="ID do filme")
    titulo: str = Field(..., description="Título do filme")
    tituloOriginal: str = Field(..., description="Título original do filme")
    capa: str = Field(..., description="URL ou caminho da imagem da capa")
    descricao: str = Field(..., min_length=10, max_length=1000, description="Descrição do filme")
    avaliacao: float = Field(..., ge=0, le=10, description="Nota média do filme (0 a 10)")
    ano: int = Field(..., ge=1800, le=2100, description="Ano de lançamento do filme")
    generos: List[str] = Field(..., description="Lista de gêneros do filme")
    diretor: str = Field(..., description="Nome do diretor do filme")

    @classmethod
    def from_entity(cls, filme):
        return cls(
            id=filme.id,
            titulo=filme.titulo,
            tituloOriginal=filme.tituloOriginal,
            capa=filme.capa,
            descricao=filme.descricao,
            avaliacao=filme.avaliacao,
            ano=filme.ano,
            generos=filme.generos,
            diretor=filme.diretor,
        )

