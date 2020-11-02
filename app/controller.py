from typing import List
from fastapi import status, APIRouter
from models import Provider
import service

router = APIRouter()

@router.get("/", response_model=List[Provider], status_code = status.HTTP_200_OK)
async def get_providers(skip: int = 0, take: int = 20):
    return await service.get_providers()    

@router.get("/{provider_id}/",response_model=Provider,status_code = status.HTTP_200_OK)
async def get_provider(provider_id: int):
    return await service.get_provider(provider_id)