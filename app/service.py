from db import database,ProviderTable,MedicareDataTable
from sqlalchemy.sql import select

async def get_providers(skip: int = 0, take: int = 20):
    query = ProviderTable.select().offset(skip).limit(take)
    return await database.fetch_all(query)    

async def get_provider(provider_id: int):
    # query = database.query(ProviderTable).filter(ProviderTable.c.id == provider_id)
    query = select([ProviderTable]).where(ProviderTable.id == provider_id)
    print(await database.fetch_one(query))
    return await database.fetch_one(query)