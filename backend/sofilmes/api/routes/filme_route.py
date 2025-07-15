from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sofilmes.usecases.filme.get_all_filme import GetAllFilmeUseCase
from sofilmes.usecases.filme.get_by_id_filme import GetByIdFilmeUseCase
from sofilmes.usecases.filme.create_filme import CreateFilmeUseCase
from sofilmes.api.schemas.filme_schema import (
    filme_to_output,
    FilmeInput,
    FilmeOutput,
    filmes_to_output,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sofilmes.api.deps import get_db_session, get_current_user
from sofilmes.domain.entities.usuario import Usuario
from typing import List
from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sofilmes.api.deps import get_filmes_repository
from sofilmes.domain.entities.filme import Filme
import uuid
from sofilmes.usecases.filme.get_filmes_mais_avaliados import GetFilmesMaisAvaliados
from sofilmes.usecases.filme.get_ultimos_filmes import GetUltimosFilmesUseCase

security = HTTPBearer()
router = APIRouter()

# TODO: Adicionar types de retorno da rotas



@router.get("/", response_model=List[FilmeOutput])
async def get_all_filmes(
    filme_repo: FilmesRepository = Depends(get_filmes_repository),
):
    usecase = GetAllFilmeUseCase(filme_repo)
    filmes = await usecase.execute()
    return filmes_to_output(filmes)


@router.get("/ultimos", response_model=List[FilmeOutput])
async def get_ultimos_filmes(
    filme_repo: FilmesRepository = Depends(get_filmes_repository),
):
    usecase = GetUltimosFilmesUseCase(filme_repo)
    filmes = await usecase.execute()

    return filmes_to_output(filmes)


@router.get("/maisAvaliados", response_model=List[FilmeOutput])
async def get_mais_avaliados(
    filme_repo: FilmesRepository = Depends(get_filmes_repository),
):
    usecase = GetFilmesMaisAvaliados(filme_repo)
    result = await usecase.execute()

    return filmes_to_output(result)


@router.get("/{filme_id}", response_model=FilmeOutput)
async def get_filme_by_id(
    filme_id: str, filme_repo: FilmesRepository = Depends(get_filmes_repository)
):
    usecase = GetByIdFilmeUseCase(filme_repo)
    filme = await usecase.execute(filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme not found")
    return filme_to_output(filme)


@router.post("/", response_model=FilmeOutput)
async def create_filme(
    data: FilmeInput,
    db: AsyncSession = Depends(get_db_session),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user: Usuario = Depends(get_current_user),
    filme_repo: FilmesRepository = Depends(get_filmes_repository),
):
    usecase = CreateFilmeUseCase(filme_repo)
    filme = Filme(
        id=str(uuid.uuid4()),
        titulo=data.titulo,
        tituloOriginal=data.tituloOriginal,
        capa=data.capa,
        descricao=data.descricao,
        avaliacao=data.avaliacao,
        ano=data.ano,
        generos=data.generos,
        diretor=data.diretor,
    )
    created_filme = await usecase.execute(filme)

    if not created_filme:
        raise HTTPException(status_code=404, detail="Filme not created")
    return filme_to_output(created_filme)
