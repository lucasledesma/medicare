from typing import List
from fastapi import status, APIRouter, HTTPException, status, Depends
from .schemas import Provider
from . import service
from sqlalchemy.orm import Session
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Provider], status_code=status.HTTP_200_OK)
async def get_providers(skip: int = 0, take: int = 20, db: Session = Depends(get_db)):
    return await service.get_providers_all(db, skip, take)


@router.get("/{provider_id}/", response_model=Provider, status_code=status.HTTP_200_OK)
async def get_provider(provider_id: int, db: Session = Depends(get_db)):
    result = await service.get_provider_by_id(db, provider_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Provider not found")
    else:
        return result
