from dataclasses import dataclass
from datetime import date

from asyncpg import UniqueViolationError
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from api_project.aplication.moderation.interfaces import ModerationInterface


@dataclass
class ModerationService:
    moderation_interface: ModerationInterface

    async def add_rates(
        self,
        rates_map: list[dict[str, str | date]]
    ) -> None:
        try:
            return await self.moderation_interface.create_rates(rates_map)
        except UniqueViolationError:
            raise HTTPException(
                status_code=404,
                detail="Тариф с заданными параметрами уже существует",
            )
        except IntegrityError:
            raise HTTPException(
                status_code=404,
                detail="Тариф с заданными параметрами уже существует",
            )
        except Exception as e:
            # Обработка других возможных ошибок
            print(f"Неожиданная ошибка: {e}")



