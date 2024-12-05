from pydantic import BaseModel


class RequestRate(BaseModel):
    cargo_type: str
    rate: float
