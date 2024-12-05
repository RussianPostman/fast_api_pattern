from api_project.adapters.db import Settings as DBSettings
from api_project.adapters.db.repositories.moderation import ModerationRepository
from api_project.adapters.db.repositories.rates import RateRepository
from api_project.aplication.moderation.services import ModerationService
from api_project.aplication.rates.services import RateService

db_settings = DBSettings()


rate_repository = RateRepository(db_settings.DATABASE_URL)
moderation_repository = ModerationRepository(db_settings.DATABASE_URL)

rate_service = RateService(rate_repository)
moderation_service = ModerationService(moderation_repository)


def get_rate_service() -> RateService:
    return rate_service


def get_moderation_service() -> ModerationService:
    return moderation_service
