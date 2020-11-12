from typing import List, Optional
from fastapi import status, APIRouter, HTTPException, status, Depends,Query,Path
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
async def get_providers(skip: int = 0, take: int =  Query(20, le=100, ge=0),
                        firstname: Optional[str] = None,
                        lastname: Optional[str] = None,
                        hcpcs_code: Optional[str] = None,
                        db: Session = Depends(get_db)):
    return await service.get_providers_all(db, skip, take, firstname, lastname, hcpcs_code)


@router.get("/{provider_id}/", response_model=Provider, status_code=status.HTTP_200_OK)
async def get_provider(provider_id: int = Path(...,ge=0), db: Session = Depends(get_db)):
    result = await service.get_provider_by_id(db, provider_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Provider not found")
    else:
        return result
