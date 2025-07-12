from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sofilmes.infra.models.avaliacao_model import AvaliacaoModel
from sqlalchemy.orm import joinedload
from sofilmes.domain.entities.avaliacao import Avaliacao


class SQLAlchemyAvaliacaoRepository(AvaliacoesRepository):
    def __init__(self, session=AsyncSession):
        self.__session = session

    async def getAvaliacoesByFilme(self, filme_id: str):
        smpt = (
            select(AvaliacaoModel)
            .where(AvaliacaoModel.filme_id == filme_id)
            .options(joinedload(AvaliacaoModel.user))
        )

        result = await self.__session.execute(smpt)

        return [avaliacao.to_entity() for avaliacao in result.unique().scalars().all()]

    async def getAvaliacao(self, avaliacao_id: str):
        smpt = select(AvaliacaoModel).where(AvaliacaoModel.id == avaliacao_id)

        result = await self.__session.execute(smpt)

        model = result.scalar_one_or_none()
        return model.to_entity()

    async def getUltimasAvaliacoes(self):
        smpt = (
            select(AvaliacaoModel)
            .options(joinedload(AvaliacaoModel.user), joinedload(AvaliacaoModel.filme))
            .order_by(AvaliacaoModel.data.desc())
            .limit(10)
        )
        result = await self.__session.execute(smpt)

        # print([avaliacao.to_entity() for avaliacao in result.unique().scalars().all()]) deu certo

        return [avaliacao.to_entity() for avaliacao in result.unique().scalars().all()]

    async def getAvaliacoesByUser(self, user_id: str):
        smpt = (
            select(AvaliacaoModel)
            .where(AvaliacaoModel.user_id == user_id)
            .options(joinedload(AvaliacaoModel.user), joinedload(AvaliacaoModel.filme))
        )

        result = await self.__session.execute(smpt)

        return [avaliacao.to_entity() for avaliacao in result.unique().scalars().all()]

    async def getAvaliacaoByUserEFilme(self, user_id: str, filme_id: str):
        smpt = (
            select(AvaliacaoModel)
            .where(
                AvaliacaoModel.filme_id == filme_id
                and AvaliacaoModel.user_id == user_id
            )
            .options(joinedload(AvaliacaoModel.user))
        )

        result = await self.__session.execute(smpt)

        return [avaliacao.to_entity() for avaliacao in result.unique().scalars().all()]

    async def criarAvaliacao(self, avaliacao: Avaliacao):
        model = AvaliacaoModel.from_entity(avaliacao)
        print(model.data)
        self.__session.add(model)
        await self.__session.commit()
        await self.__session.refresh(model)

        avaliacao.id = model.id

        return model.to_entity()

    async def editarAvaliacao(self, avaliacao: Avaliacao):
        model = AvaliacaoModel.from_entity(avaliacao)
        await self.__session.execute(
            update(AvaliacaoModel)
            .where(AvaliacaoModel.id == avaliacao.id)
            .values(model)
        )
        await self.__session.commit()
        await self.__session.refresh(model)

        return model.to_entity()

    async def removerAvaliacao(self, avaliacao_id: str):
        await self.__session.execute(
            delete(AvaliacaoModel).where(AvaliacaoModel.id == avaliacao_id)
        )
        await self.__session.commit()

        return True
