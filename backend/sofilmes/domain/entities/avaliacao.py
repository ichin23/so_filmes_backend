import datetime

class Avaliacao:
    def __init__(
        self, id: str, user_id: str, filme_id: str, data: datetime.datetime, avaliacao: float, comentario: str
    ):
        self.id = id
        self.user_id = user_id
        self.filme_id = filme_id
        self.data = data
        self.avaliacao = avaliacao
        self.comentario = comentario
