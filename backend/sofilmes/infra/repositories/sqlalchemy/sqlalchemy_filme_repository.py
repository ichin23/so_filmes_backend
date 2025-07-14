from sofilmes.domain.repositories.filmes_repositories import FilmesRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from datetime import datetime, timedelta
from sofilmes.infra.models.filme_model import FilmeModel
from sofilmes.domain.entities.filme import Filme
from sofilmes.infra.models.avaliacao_model import AvaliacaoModel


class SQLAlchemyFilmeRepository(FilmesRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_all(self, limit: int = 10):
        smpt = select(FilmeModel).limit(limit)
        result = await self.__session.execute(smpt)

        return [filme.to_entity() for filme in result.unique().scalars().all()]

    async def get_ultimos_filmes(self):
        smpt = select(FilmeModel).order_by(FilmeModel.ano).limit(15)
        result = await self.__session.execute(smpt)

        return [filme.to_entity() for filme in result.unique().scalars().all()]

    async def get_mais_avaliados(self):
        seven_days_ago = datetime.now() - timedelta(days=7)

        avaliacao_counts = (
            select(
                AvaliacaoModel.filme_id,
                func.count(AvaliacaoModel.id).label("avaliacao_count"),
            )
            # Filter for evaluations in the last 7 days
            .where(AvaliacaoModel.data >= seven_days_ago)
            # Group by the movie ID
            .group_by(AvaliacaoModel.filme_id)
            # Order by the count in descending order
            .order_by(func.count(AvaliacaoModel.id).desc())
            # Limit to the top 10 movies
            .limit(10)
            # Make this a subquery
            .subquery()
        )
        stmt = (
            select(FilmeModel).join(
                avaliacao_counts, FilmeModel.id == avaliacao_counts.c.filme_id
            )
            # Order the final result based on the count from the subquery
            .order_by(avaliacao_counts.c.avaliacao_count.desc())
        )

        result = await self.__session.execute(stmt)

        return [filme.to_entity() for filme in result.unique().scalars().all()]

    async def get_by_id(self, filme_id: str):
        smpt = select(FilmeModel).where(FilmeModel.id == filme_id)
        result = await self.__session.execute(smpt)

        return result.scalar_one_or_none()

    async def create(self, filme: Filme):
        model = FilmeModel.from_entity(filme)
        self.__session.add(model)
        await self.__session.commit()
        await self.__session.refresh(model)
        filme.id = model.id
        return model.to_entity()
