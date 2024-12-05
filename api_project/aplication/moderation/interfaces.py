from abc import ABC, abstractmethod

from datetime import datetime, date

from api_project.adapters.db.models import Rate


class ModerationInterface(ABC):

    @abstractmethod
    async def create_rates(
        self,
        mappings: list[dict[str, str | date]]
    ):
        """
        Создаёт несколько объектов Rate
        """
        ...
