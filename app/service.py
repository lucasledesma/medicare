from db import database,ProviderTable,MedicareDataTable,Session
from sqlalchemy.sql import select
import json
from fastapi.encoders import jsonable_encoder

async def get_providers(skip: int = 0, take: int = 20):
    query = ProviderTable.select().offset(skip).limit(take)
    return await database.fetch_all(query)    

async def get_provider(provider_id: int):
    session = Session()
    result=session.query(ProviderTable).first()
    #print(jsonable_encoder(result.medicaredata))
    return result
