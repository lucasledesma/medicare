from .db import ProviderTable,Session
from sqlalchemy.sql import select

async def get_providers_all(skip: int, take: int):
    result = Session().query(ProviderTable).offset(skip).limit(take).all()
    return result

async def get_provider_by_id(provider_id: int):
    result = Session().query(ProviderTable).first()
    return result
