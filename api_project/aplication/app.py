from api_project.adapters.db import Settings as DBSettings
from api_project.adapters.db.repositories.rates import RateRepository
from api_project.aplication.rates.services import RateService

db_settings = DBSettings()


rate_repository = RateRepository(db_settings.DATABASE_URL)

rate_service = RateService(rate_repository)


def get_rate_service() -> RateService:
    return rate_service
