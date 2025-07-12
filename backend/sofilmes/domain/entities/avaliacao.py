import datetime
from typing import Optional, TYPE_CHECKING
from sofilmes.domain.entities.filme import Filme

if TYPE_CHECKING:
    from sofilmes.domain.entities.usuario import Usuario


class Avaliacao:
    def __init__(
        self,
        id: str,
        user_id: str,
        filme_id: str,
        data: datetime.datetime,
        avaliacao: float,
        comentario: str,
        user: Optional["Usuario"] = None,
        filme: Optional["Filme"] = None,
    ):
        self.id = id
        self.user_id = user_id
        self.filme_id = filme_id
        self.data = data
        self.avaliacao = avaliacao
        self.comentario = comentario
        self.user = user
        self.filme = filme
