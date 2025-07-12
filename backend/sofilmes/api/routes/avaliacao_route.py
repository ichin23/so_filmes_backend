import datetime
from fastapi import APIRouter, Depends, HTTPException
from sofilmes.usecases.avaliacao.criar_avaliacao import CriarAvaliacaoUseCase
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sofilmes.usecases.avaliacao.get_avaliacao import GetAvaliacaoUseCase
from sofilmes.usecases.avaliacao.get_avaliacoes_by_usuario import (
    GetAvaliacoesByUsuarioUseCase,
)
from sofilmes.usecases.avaliacao.remover_avaliacao import RemoverAvaliacao
from sofilmes.usecases.avaliacao.editar_avaliacao import EditarAvaliacaoUseCase
from sofilmes.api.schemas.avaliacao_schema import (
    avaliacao_to_output,
    AvaliacaoOutput,
    avaliacoes_to_output,
    CreateAvaliacaoInput,
)
from typing import List
from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.api.deps import get_avaliacao_repository, get_current_user
from sofilmes.domain.entities.avaliacao import Avaliacao
import uuid
from sofilmes.domain.entities.usuario import Usuario
from sofilmes.usecases.avaliacao.get_ultimas_avaliacoes import (
    GetUltimasAvaliacoesUseCase,
)

security = HTTPBearer()
router = APIRouter()

# TODO: Adicionar types de retorno da rotas


@router.get("/byuser/", response_model=List[AvaliacaoOutput])
async def get_avaliacoes_by_user(
    avaliacao_repo: AvaliacoesRepository = Depends(get_avaliacao_repository),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user: Usuario = Depends(get_current_user),
):
    usecase = GetAvaliacoesByUsuarioUseCase(avaliacao_repo)
    avaliacoes = await usecase.execute(user.id)
    return avaliacoes_to_output(avaliacoes)


@router.get("/byid/{avaliacao_id}", response_model=AvaliacaoOutput)
async def get_avaliacao_by_id(
    avaliacao_id: str,
    avaliacao_repo: AvaliacoesRepository = Depends(get_avaliacao_repository),
):
    usecase = GetAvaliacaoUseCase(avaliacao_repo)
    avaliacao = await usecase.execute(avaliacao_id)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação not found")
    return avaliacao_to_output(avaliacao)


@router.get("/ultimas", response_model=List[AvaliacaoOutput])
async def get_ultimas_avaliacoes(
    avaliacao_repo: AvaliacoesRepository = Depends(get_avaliacao_repository),
):
    usecase = GetUltimasAvaliacoesUseCase(avaliacao_repo)
    avaliacoes = await usecase.execute()
    print(avaliacoes[0].user)
    return avaliacoes_to_output(avaliacoes)


@router.post("/", response_model=AvaliacaoOutput)
async def create_avaliacao(
    data: CreateAvaliacaoInput,
    avaliacao_repo: AvaliacoesRepository = Depends(get_avaliacao_repository),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user: Usuario = Depends(get_current_user),
):
    usecase = CriarAvaliacaoUseCase(avaliacao_repo)
    avaliacao = Avaliacao(
        id=str(uuid.uuid4()),
        user_id=user.id,
        filme_id=data.filme_id,
        data=datetime.datetime.now(),
        avaliacao=data.avaliacao,
        comentario=data.comentario,
    )

    created_avaliacao = await usecase.execute(avaliacao)
    if not created_avaliacao:
        raise HTTPException(status_code=400, detail="Failed to add avaliacao")
    return avaliacao_to_output(created_avaliacao)


@router.delete("/{avaliacao_id}")
async def delete_avaliacao(
    avaliacao_id: str,
    avaliacao_repo: AvaliacoesRepository = Depends(get_avaliacao_repository),
):
    # print(" ID recebido para deletar:", avaliacao_id)
    # print(" IDs existentes:", list(repo._avaliacoes.keys()))

    usecase = RemoverAvaliacao(avaliacao_repo)
    success = await usecase.execute(avaliacao_id)

    # print(" ID recebido para deletar:", avaliacao_id)
    # print(" IDs existentes:", list(repo._avaliacoes.keys()))
    if not success:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return {"message": "Avaliação deletada com sucesso"}


@router.put("/{avaliacao_id}", response_model=AvaliacaoOutput)
async def update_avaliacao(
    avaliacao_id: str,
    data: CreateAvaliacaoInput,
    avaliacao_repo: AvaliacoesRepository = Depends(get_avaliacao_repository),
    credentials: HTTPAuthorizationCredentials = Depends(security),
):

    usecaseGet = GetAvaliacaoUseCase(avaliacao_repo)
    existing_avaliacao = usecaseGet.execute(avaliacao_id)

    if not existing_avaliacao:
        raise HTTPException(status_code=404, detail="Post not found")

    updated_avaliacao = Avaliacao(
        id=avaliacao_id,
        user_id=data.user_id,
        filme_id=data.filme_id,
        data=datetime.datetime.now(),
        comentario=data.comentario,
        avaliacao=data.avaliacao,
    )
    usecase = EditarAvaliacaoUseCase(avaliacao_repo)

    success = await usecase.execute(updated_avaliacao)
    if not success:
        raise HTTPException(status_code=400, detail="Avaliação não atualizada")

    return avaliacao_to_output(success)
