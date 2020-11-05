from sqlalchemy.orm import Session
from sqlalchemy import or_
from .models import MedicareDataTable, ProviderTable

async def get_providers_all(db: Session, skip: int, take: int, firstname: str, lastname: str, hcpcs_code:str, searchQuery: str):
    result = db.query(ProviderTable).join(MedicareDataTable). filter(
                or_(ProviderTable.firstname==firstname,firstname is None) &
                or_(ProviderTable.lastname==lastname,lastname is None) &
                or_(MedicareDataTable.hcpcs_code=="99217") &
                or_(ProviderTable.firstname.ilike(f"%{searchQuery}%"),searchQuery is None) &
                or_(ProviderTable.lastname.ilike(f"%{searchQuery}%"),searchQuery is None)
            
            ).offset(skip).limit(take).all()
    return result

async def get_provider_by_id(db: Session, provider_id: int):
    result = db.query(ProviderTable).filter(ProviderTable.id==provider_id).first()
    return result
