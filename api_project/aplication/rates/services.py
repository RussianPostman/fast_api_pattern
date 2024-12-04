from dataclasses import dataclass
from datetime import datetime

from fastapi import HTTPException

from api_project.aplication.rates.interfaces import RateInterface
from api_project.domain.rates import RateCalculations


@dataclass
class RateService:
    rate_interface: RateInterface

    async def get_rate(
        self,
        name: str,
        date: datetime,
        amount_of_insurance: float,
    ) -> float:
        rate_response = await self.rate_interface.get_rate(name, date)

        if rate_response:
            actual_rate = rate_response[0]
        else:
            raise HTTPException(status_code=400, detail=f"Item {name} not found")

        return RateCalculations.base_calculation(
            amount_of_insurance, actual_rate.rate
        )
