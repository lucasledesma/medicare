from db import database,ProviderTable,MedicareDataTable,Session
from sqlalchemy.sql import select
import json
from fastapi.encoders import jsonable_encoder

async def get_providers(skip: int, take: int):
    result = Session().query(ProviderTable).offset(skip).limit(take).all()
    #print(jsonable_encoder(result))
    return result    

async def get_provider(provider_id: int):
    result = Session().query(ProviderTable).first()
    #print(jsonable_encoder(result))
    return result
