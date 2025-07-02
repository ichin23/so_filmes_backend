from sqlalchemy import Column, String, Integer
from sofilmes.infra.database import Base

class AvaliacaoModel(Base):
    __tablename__ = "avaliacoes"

    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    filme_id = Column(String, nullable=False)
    comentario = Column(String, nullable=False)
    quant = Column(Integer, nullable=False)
    data = Column(String, nullable=False)
