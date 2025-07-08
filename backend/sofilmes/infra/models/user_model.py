import  sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sofilmes.infra.database import Base
from sofilmes.domain.entities.usuario import Usuario
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password
import uuid
from sofilmes.domain.entities.usuario import Usuario

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(sa.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome: Mapped[str] = mapped_column(sa.String, nullable=False)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(sa.String, nullable=False)

    avaliacoes = sa.orm.relationship("AvaliacaoModel", back_populates="user", cascade="all, delete")

    @classmethod
    def from_entity(cls, entity: Usuario) -> "UserModel":
        return cls(
            id=entity.id,
            nome=entity.nome,
            email=entity.email.value,
            senha=entity.senha.value
        )

    def to_entity(self) -> Usuario:
        
        return Usuario(
            id=self.id,
            nome=self.nome,
            username=self.username,
            email=Email(self.email),
            senha=Password(self.senha)
        )