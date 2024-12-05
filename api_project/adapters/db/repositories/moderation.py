from datetime import date

from sqlalchemy import insert

from api_project.adapters.db.models import Rate
from api_project.adapters.db.repositories import BaseRepository
from api_project.aplication.moderation.interfaces import ModerationInterface


class ModerationRepository(BaseRepository, ModerationInterface):
    async def create_rates(
            self,
            mappings: list[dict[str, str | date]]
    ):
        async with self.get_session_maker()() as session:
            async with session.begin():
                await session.execute(
                    insert(Rate).values(mappings)
                )
