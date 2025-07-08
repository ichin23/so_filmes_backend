import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from sofilmes.infra.database import Base
from typing import List
from sofilmes.domain.entities.filme import Filme


class FilmeModel(Base):
    __tablename__ = "filmes"

    id: Mapped[str] = mapped_column(sa.String, primary_key=True)
    titulo: Mapped[str] = mapped_column(sa.String, nullable=False)
    tituloOriginal: Mapped[str] = mapped_column(sa.String, nullable=False)
    capa: Mapped[str] = mapped_column(sa.String, nullable=False)
    descricao: Mapped[str] = mapped_column(sa.String, nullable=False)
    avaliacao: Mapped[float] = mapped_column(sa.Float, nullable=False)
    ano: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    generos: Mapped[List[str]] = mapped_column(ARRAY(sa.String), nullable=False)
    diretor: Mapped[str] = mapped_column(sa.String, nullable=False)

    @classmethod
    def from_entity(cls, entity: Filme) -> "FilmeModel":
        return cls(
            id=entity.id,
            titulo=entity.titulo,
            tituloOriginal=entity.tituloOriginal,
            capa=entity.capa,
            descricao=entity.descricao,
            avaliacao=entity.avaliacao,
            ano=entity.ano,
            generos=entity.generos,
            diretor=entity.diretor,
        )

    def to_entity(self) -> Filme:
        return Filme(
            id=self.id,
            titulo=self.titulo,
            tituloOriginal=self.tituloOriginal,
            capa=self.capa,
            descricao=self.descricao,
            avaliacao=self.avaliacao,
            ano=self.ano,
            generos=self.generos,
            diretor=self.diretor,
        )
