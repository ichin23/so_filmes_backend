from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sofilmes.infra.database import Base

class FilmeModel(Base):
    __tablename__ = "filmes"

    id = Column(String, primary_key=True)
    titulo = Column(String, nullable=False)
    tituloOriginal = Column(String, nullable=False)
    capa = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    avaliacao = Column(Float, nullable=False)
    ano = Column(Integer, nullable=False)
    generos = Column(ARRAY(String), nullable=False)
    diretor = Column(String, nullable=False)
