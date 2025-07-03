from fastapi import APIRouter, Depends
from sofilmes.usecases.filme.get_all_filme import GetAllFilmeUseCase
from sofilmes.usecases.filme.get_by_id_filme import GetByIdFilmeUseCase
from sofilmes.usecases.filme.create_filme import CreateFilmeUseCase
from sofilmes.api.schemas.filme_schema import FilmeInput, FilmeOutput
from typing import List
from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.api.deps import filme_repo
from sofilmes.domain.entities.filme import Filme
import uuid

router = APIRouter()

#TODO: Adicionar types de retorno da rotas

@router.get("/", response_model=List[FilmeOutput])
def get_all_filmes():
    usecase = GetAllFilmeUseCase()
    filmes = usecase.execute()
    return filmes

@router.get("/{filme_id}", response_model=FilmeOutput)
def get_filme_by_id(filme_id: str):
    usecase = GetByIdFilmeUseCase()
    filme = usecase.execute()
    return filme

@router.post("/", response_model=FilmeOutput)
async def create_filme(
    data: FilmeInput,
    #db: AsyncSession = Depends(get_db_session)
    #credentials: HTTPAuthorizationCredentials = Depends(security)
    filme_repo: FilmesRepository = Depends(filme_repo)
):
    usecase = CreateFilmeUseCase(filme_repo)
    filme = Filme(
        id=str(uuid.uuid4),
        titulo=data.titulo,
        tituloOriginal=data.tituloOriginal,
        capa=data.capa,
        descricao=data.descricao,
        avaliacao=data.avaliacao,
        ano=data.ano,
        generos=data.generos,
        diretor=data.diretor
    )
    created_filme = await usecase.execute()
    return created_filme