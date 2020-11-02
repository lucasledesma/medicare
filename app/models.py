from pydantic import BaseModel, Field
from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)

class MedicareData(BaseModel):
    #id: int
    #provider_id: int
    hcpcs_code: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Provider(BaseModel):
    id: int = Field(alias='National Provider Identifier')    
    lastname: Optional[str] = Field(alias='Last Name/Organization Name of the Provider')   
    firstname: Optional[str] = Field(alias='First Name of the Provider') 
    middle_initial: Optional[str] = Field(alias='Middle Initial of the Provider')
    credentials: Optional[str] = Field(alias="Credentials of the Provider")
    gender: Optional[str] = Field(alias="Gender of the Provider")
    entity_type: Optional[str] = Field(alias="Entity Type of the Provider")
    street_address_1: Optional[str] = Field(alias='Street Address 1 of the Provider')
    street_address_2:Optional[str] = Field(alias="Street Address 2 of the Provider")
    city: Optional[str] = Field(alias="City of the Provider")
    zip_code: Optional[str] = Field(alias="Zip Code of the Provider")
    state_code:Optional[str] = Field(alias= "State Code of the Provider")
    country_code: Optional[str] = Field(alias="Country Code of the Provider")
    provider_type: Optional[str] = Field(alias="Provider Type")
    medicare_participation_indicator:Optional[str] = Field(alias= "Medicare Participation Indicator")
    #hcpcs_code:List[Optional[str]] = Field(alias= "HCPCS Code" )
    medicaredata: List[MedicareData]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

