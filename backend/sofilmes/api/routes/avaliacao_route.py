from fastapi import APIRouter, Depends, HTTPException
from sofilmes.usecases.avaliacao.add_avaliacao import CreateAvalicaoUseCase
from fastapi.security import HTTPAuthorizationCredentials
from sofilmes.usecases.avaliacao.get_avaliacao import GetAvaliacaoUseCase
from sofilmes.usecases.avaliacao.get_avaliacao_by_user import GetAvaliacaoByUserUseCase
from sofilmes.usecases.avaliacao.delete_avaliacao import DeleteAvaliacaoUseCase
from sofilmes.usecases.avaliacao.set_avaliacao import SetAvaliacaoUseCase
from sofilmes.api.schemas.avaliacao_schema import AvaliacaoOutput, CreateAvaliacaoInput
from typing import List
from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sofilmes.api.deps import avaliacao_repo
from sofilmes.domain.entities.avaliacao import Avaliacao
import uuid
from sofilmes.usecases.avaliacao.set_avaliacao import SetAvaliacaoUseCase


router = APIRouter()

#TODO: Adicionar types de retorno da rotas

@router.get("/byuser/{id_user}", response_model=List[AvaliacaoOutput])
def get_avaliacoes_by_user(id_user:str):
    usecase = GetAvaliacaoByUserUseCase(avaliacao_repo())
    avaliacoes = usecase.execute(id_user)
    return avaliacoes

@router.get("/byid/{avaliacao_id}", response_model=AvaliacaoOutput)
def get_avaliacao_by_id(avaliacao_id: str):
    usecase = GetAvaliacaoUseCase(avaliacao_repo())
    avaliacao = usecase.execute(avaliacao_id)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação not found")
    return avaliacao

@router.post("/", response_model=AvaliacaoOutput)
def create_avaliacao( data: CreateAvaliacaoInput,):
    usecase = CreateAvalicaoUseCase(avaliacao_repo())
    avaliacao = Avaliacao(
        id=str(uuid.uuid4()),
        user_id=data.user_id,
        filme_id=data.filme_id,
        avaliacao = data.avaliacao,
        comentario = data.comentario,
    )

    created_avaliacao = usecase.execute(avaliacao)
    return AvaliacaoOutput.from_entity(created_avaliacao)


@router.delete("/{avaliacao_id}")
def delete_avaliacao(
    avaliacao_id: str,
    repo: AvaliacoesRepository = Depends(avaliacao_repo),
):
    #print(" ID recebido para deletar:", avaliacao_id)
    #print(" IDs existentes:", list(repo._avaliacoes.keys()))  

    usecase = DeleteAvaliacaoUseCase(repo)
    success = usecase.execute(avaliacao_id)
    
    #print(" ID recebido para deletar:", avaliacao_id)
    #print(" IDs existentes:", list(repo._avaliacoes.keys()))
    if not success:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return {"message": "Avaliação deletada com sucesso"}


@router.put("/{avaliacao_id}", response_model=AvaliacaoOutput)
def update_avaliacao(avaliacao_id: str, data: CreateAvaliacaoInput):
    repo = avaliacao_repo()
    usecase = SetAvaliacaoUseCase(repo)

    avaliacao = Avaliacao(
        id=avaliacao_id,
        user_id=data.user_id,
        filme_id=data.filme_id,
        comentario=data.comentario,
        avaliacao=data.avaliacao,
    )

    success = usecase.execute(avaliacao)
    if not success:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada para atualização")

    return AvaliacaoOutput.from_entity(avaliacao)



