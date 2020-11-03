from sqlalchemy.orm import Session
from .models import ProviderTable

async def get_providers_all(db: Session, skip: int, take: int):
    result = db.query(ProviderTable).offset(skip).limit(take).all()
    return result

async def get_provider_by_id(db: Session, provider_id: int):
    result = db.query(ProviderTable).filter(ProviderTable.id==provider_id).first()
    return result
