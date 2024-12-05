from datetime import date

from fastapi import APIRouter, Depends, Body

from api_project.adapters.api.moderation.schemes import RequestRate
from api_project.aplication.app import get_moderation_service
from api_project.aplication.moderation.services import ModerationService

moderation_router = APIRouter(
   prefix="/moderation",
   tags=["Управление"],
)


@moderation_router.post("/add_rates")
async def insurance_costs(
    request: dict[date, list[RequestRate]] = Body(),
    moderation_service: ModerationService = Depends(get_moderation_service)
) -> None:
    items_map = []

    for rate_date in request.keys():
        items_map += [
            {'date_to': rate_date, 'name': rate.cargo_type, 'rate': rate.rate}
            for rate in request[rate_date]
        ]

    return await moderation_service.add_rates(items_map)
