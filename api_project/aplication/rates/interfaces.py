from abc import ABC, abstractmethod

from datetime import datetime

from api_project.adapters.db.models import Rate


class RateInterface(ABC):

    @abstractmethod
    async def get_rate(self, name: str, date: datetime) -> list[Rate]:
        """
        По названию категории и дате выдаёт ставку страхования. Если
        по имени не нашлось тарифов, возвращается тариф для категории Other
        """
        ...
