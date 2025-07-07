class Avaliacao:
    def __init__(self, id: str, user_id: str, filme_id: str, avaliacao: float, comentario: str):
        self.id = id
        self.user_id = user_id
        self.filme_id = filme_id
        self.avaliacao = avaliacao
        self.comentario = comentario
