from datetime import datetime

from pydantic import BaseModel


class InsuranceCostsRequest(BaseModel):
    name: str
    date: datetime
    amount: float


class InsuranceCostsResponse(BaseModel):
    name: str
    amount_of_insurance: float
    price_of_insurance: float
