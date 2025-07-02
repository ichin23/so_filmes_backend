from fastapi import APIRouter
from sofilmes.usecases.filme.get_all_filme import GetAllFilmeUseCase
from sofilmes.usecases.filme.get_by_id_filme import GetByIdFilmeUseCase

router = APIRouter()

#TODO: Adicionar types de retorno da rotas

@router.get("/")
def get_all_filmes():
    usecase = GetAllFilmeUseCase()
    filmes = usecase.execute()
    return filmes

@router.get("/{filme_id}")
def get_filme_by_id(filme_id: str):
    usecase = GetByIdFilmeUseCase()
    filme = usecase.execute()
    return filme