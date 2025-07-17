from sofilmes.domain.repositories.avaliacoes_repositories import AvaliacoesRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, func
from sofilmes.infra.models.avaliacao_model import AvaliacaoModel
from sqlalchemy.orm import joinedload
from sofilmes.domain.entities.avaliacao import Avaliacao
from sofilmes.infra.models.filme_model import FilmeModel
from sofilmes.infra.models.user_model import UserModel
from sqlalchemy.orm import selectinload


class SQLAlchemyAvaliacaoRepository(AvaliacoesRepository):
    def __init__(self, session=AsyncSession):
        self.__session = session

    async def getAvaliacoesByFilme(self, filme_id: str):
        smpt = (
            select(AvaliacaoModel)
            .where(AvaliacaoModel.filme_id == filme_id)
            .options(joinedload(AvaliacaoModel.user), joinedload(AvaliacaoModel.filme))
        )

        result = await self.__session.execute(smpt)

        return [avaliacao.to_entity() for avaliacao in result.unique().scalars().all()]

    async def getAvaliacao(self, avaliacao_id: str):
        stmt = (
            select(AvaliacaoModel)
            .options(
                selectinload(AvaliacaoModel.user), 
                selectinload(AvaliacaoModel.filme)  
            )
            .where(AvaliacaoModel.id == avaliacao_id)
        )

        result = await self.__session.execute(stmt)

        model = result.scalar_one_or_none()
        if model is None:
            return None
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
                AvaliacaoModel.filme_id == filme_id, AvaliacaoModel.user_id == user_id
            )
            .options(joinedload(AvaliacaoModel.user), joinedload(AvaliacaoModel.filme))
        )

        result = await self.__session.execute(smpt)

        return result.unique().scalar_one_or_none().to_entity()

    async def criarAvaliacao(self, avaliacao: Avaliacao):
        print(f"{avaliacao.user_id} : {avaliacao.filme_id}")
        model = AvaliacaoModel.from_entity(avaliacao)
        print(model.data)
        print(f"{model.user_id} : {model.filme_id}")
        self.__session.add(model)
        await self.__session.commit()

        # Calcula a nova média via SELECT
        result = await self.__session.execute(
            select(func.avg(AvaliacaoModel.quant)).where(
                AvaliacaoModel.filme_id == avaliacao.filme_id
            )
        )
        nova_media = result.scalar()

        # Atualiza o campo 'avaliacao' no filme
        await self.__session.execute(
            update(FilmeModel)
            .where(FilmeModel.id == avaliacao.filme_id)
            .values(avaliacao=nova_media)
        )

        result = await self.__session.execute(
            select(func.avg(AvaliacaoModel.quant)).where(
                AvaliacaoModel.user_id == avaliacao.user_id
            )
        )
        nova_media = result.scalar()

        # Atualiza o campo 'avaliacao' no filme
        await self.__session.execute(
            update(UserModel)
            .where(UserModel.id == avaliacao.user_id)
            .values(media=nova_media)
        )
        await self.__session.commit()

        result = await self.__session.execute(
            select(AvaliacaoModel)
            .options(joinedload(AvaliacaoModel.filme), joinedload(AvaliacaoModel.user))
            .where(AvaliacaoModel.id == model.id)
        )
        model = result.unique().scalar_one_or_none()

        avaliacao.id = model.id

        return model.to_entity()

    from sqlalchemy.orm import selectinload

    async def editarAvaliacao(self, avaliacao: Avaliacao) -> Avaliacao:
        values_to_update = {
            "user_id": avaliacao.user_id,
            "filme_id": avaliacao.filme_id,
            "comentario": avaliacao.comentario,
            "quant": avaliacao.avaliacao,
            "data": avaliacao.data,
        }

        await self.__session.execute(
            update(AvaliacaoModel)
            .where(AvaliacaoModel.id == avaliacao.id)
            .values(
                user_id=avaliacao.user_id,
                filme_id=avaliacao.filme_id,
                comentario=avaliacao.comentario,
                quant=avaliacao.avaliacao,
                data=avaliacao.data,
            )
        )
        await self.__session.commit()

        # Calcula a nova média via SELECT
        result = await self.__session.execute(
            select(func.avg(AvaliacaoModel.quant)).where(
                AvaliacaoModel.filme_id == avaliacao.filme_id
            )
        )
        nova_media = result.scalar()

        # Atualiza o campo 'avaliacao' no filme
        await self.__session.execute(
            update(FilmeModel)
            .where(FilmeModel.id == avaliacao.filme_id)
            .values(avaliacao=nova_media)
        )

        result = await self.__session.execute(
            select(func.avg(AvaliacaoModel.quant)).where(
                AvaliacaoModel.user_id == avaliacao.user_id
            )
        )
        nova_media = result.scalar()

        # Atualiza o campo 'avaliacao' no filme
        await self.__session.execute(
            update(UserModel)
            .where(UserModel.id == avaliacao.user_id)
            .values(media=nova_media)
        )
        await self.__session.commit()

        result = await self.__session.execute(
            select(AvaliacaoModel)
            .where(AvaliacaoModel.id == avaliacao.id)
            .options(joinedload(AvaliacaoModel.user), joinedload(AvaliacaoModel.filme))  # Evita o lazy loading
        )
        model = result.unique().scalar_one_or_none()

        result = await self.__session.execute(
            select(AvaliacaoModel)
            .options(selectinload(AvaliacaoModel.user), selectinload(AvaliacaoModel.filme))
            .where(AvaliacaoModel.id == avaliacao.id)
        )
        updated_model = result.scalar_one_or_none()

        if updated_model is None:
            raise Exception("Avaliação não encontrada após atualização")

        return updated_model.to_entity()



    async def removerAvaliacao(self, avaliacao_id: str):
        await self.__session.execute(
            delete(AvaliacaoModel).where(AvaliacaoModel.id == avaliacao_id)
        )
        await self.__session.commit()

        return True
