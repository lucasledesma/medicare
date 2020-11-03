from typing import List
from fastapi import status, APIRouter, HTTPException, Response, status
from starlette.status import HTTP_404_NOT_FOUND
from .models import Provider
from .service import get_providers_all, get_provider_by_id

router = APIRouter()

@router.get("/", response_model=List[Provider], status_code = status.HTTP_200_OK)
async def get_providers(skip: int = 0, take: int = 20):
    return await get_providers_all(skip,take)    

@router.get("/{provider_id}/",response_model=Provider,status_code = status.HTTP_200_OK)
async def get_provider(provider_id: int, response:Response):
    result = await get_provider_by_id(provider_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Provider not found")
    else:
        return  result