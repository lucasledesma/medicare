from typing import List
from fastapi import status, APIRouter
from .models import Provider
from .service import get_providers_all, get_provider_by_id

router = APIRouter()

@router.get("/", response_model=List[Provider], status_code = status.HTTP_200_OK)
async def get_providers(skip: int = 0, take: int = 20):
    return await get_providers_all(skip,take)    

@router.get("/{provider_id}/",response_model=Provider,status_code = status.HTTP_200_OK)
async def get_provider(provider_id: int):
    return await get_provider_by_id(provider_id)