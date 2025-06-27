class Avaliacao:
    def __init__(self, id:str, quant:int, comentario:str, user_id:str):
        self.id = id
        self.user_id = user_id
        self.quant = quant 
        self.comentario = comentario 