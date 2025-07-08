import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sofilmes.infra.database import Base
from sofilmes.domain.entities.avaliacao import Avaliacao

class AvaliacaoModel(Base):
    __tablename__ = "avaliacoes"

    id: Mapped[str] = mapped_column(sa.String, primary_key=True)
    user_id: Mapped[str] = mapped_column(sa.String, sa.ForeignKey("users.id"), nullable=False)
    filme_id: Mapped[str] = mapped_column(sa.String, sa.ForeignKey("filmes.id"), nullable=False)
    comentario: Mapped[str] = mapped_column(sa.String, nullable=False)
    quant: Mapped[float] = mapped_column(sa.Float, nullable=False)
    data: Mapped[str] = mapped_column(sa.String, nullable=False)

    user = sa.orm.relationship("UserModel", back_populates="avaliacoes")
    filme = sa.orm.relationship("FilmeModel", back_populates="avaliacoes")
    
    @classmethod
    def from_entity(cls, entity: Avaliacao) -> "AvaliacaoModel":
        return cls(
            id=entity.id,
            user_id=entity.autor_id,
            filme_id=entity.filme_id,
            comentario=entity.comentario,
            quant=entity.avaliacao,
            #TODO:data=entity.data
        )

    def to_entity(self) -> Avaliacao:
        from sofilmes.domain.entities.avaliacao import Avaliacao
        return Avaliacao(
            id=self.id,
            autor_id=self.user_id,
            filme_id=self.filme_id,
            comentario=self.comentario,
            avaliacao=self.quant,
            #data=self.data
        )
