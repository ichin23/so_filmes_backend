from sqlalchemy import String, Column
from sofilmes.infra.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)