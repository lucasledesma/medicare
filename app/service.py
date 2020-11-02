from db import database,providers

async def get_providers(skip: int = 0, take: int = 20):
    query = providers.select().offset(skip).limit(take)
    return await database.fetch_all(query)    

async def get_provider(provider_id: int):
    query = providers.select().where(providers.c.id == provider_id)
    return await database.fetch_one(query)