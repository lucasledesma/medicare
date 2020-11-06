from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from sqlalchemy.sql.selectable import subquery
from .models import MedicareDataTable, ProviderTable
from typing import  Optional

async def get_providers_all(db: Session, skip: int, take: int, firstname: Optional[str], lastname: Optional[str], hcpcs_code:Optional[str]):
    subquery = db.query(ProviderTable.id).join(MedicareDataTable).filter(
                and_((hcpcs_code is None or MedicareDataTable.hcpcs_code==hcpcs_code),
                (firstname is None or ProviderTable.firstname.like(f"%{firstname}%")),
                (lastname is None or ProviderTable.lastname.like(f"%{lastname}%")))
            ).group_by(ProviderTable.id).offset(skip).limit(take).subquery()
    result = db.query(ProviderTable).filter(ProviderTable.id.in_(subquery)).all()                
    return result

async def get_provider_by_id(db: Session, provider_id: int):
    result = db.query(ProviderTable).filter(ProviderTable.id==provider_id).first()
    return result
