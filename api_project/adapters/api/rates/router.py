from fastapi import APIRouter, Depends

from api_project.adapters.api.rates.schemes import InsuranceCostsRequest, InsuranceCostsResponse
from api_project.aplication.app import get_rate_service
from api_project.aplication.rates.services import RateService

rates_router = APIRouter(
   prefix="/rates",
   tags=["Тарифы"],
)


@rates_router.post("/insurance_costs")
async def insurance_costs(
    request: InsuranceCostsRequest = Depends(),
    rate_service: RateService = Depends(get_rate_service)
) -> InsuranceCostsResponse:
    prise = await rate_service.get_rate(request.name, request.date, request.amount)

    return InsuranceCostsResponse(
        name=request.name,
        amount_of_insurance=request.amount,
        price_of_insurance=prise,
    )
