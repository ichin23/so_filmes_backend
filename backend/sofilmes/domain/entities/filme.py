class Filme:
    def __init__(
        self,
        id: str,
        titulo: str,
        tituloOriginal: str,
        capa: str,
        descricao: str,
        avaliacao: float,
        ano: int,
        generos: list[str],
        diretor: str,
    ):
        self.id = id
        self.titulo = titulo
        self.tituloOriginal = tituloOriginal
        self.capa = capa
        self.descricao = descricao
        self.avaliacao = avaliacao
        self.ano = ano
        self.generos = generos
        self.diretor = diretor
