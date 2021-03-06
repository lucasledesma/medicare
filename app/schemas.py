from pydantic import BaseModel, Field
from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)

class MedicareData(BaseModel):
    medicare_participation_indicator: Optional[str] = Field(alias="Medicare Participation Indicator")   
    hcpcs_code: Optional[str]= Field(alias="Hcpcs code")   
    hcpcs_description: Optional[str]= Field(alias="Hcpcs Description")   
    hcpcs_drug_indicator: Optional[str]= Field(alias="Hcpcs Drug Indicator")   
    number_of_services: Optional[int]= Field(alias="Number of Services")   
    number_of_medicare_beneficiaries: Optional[int]= Field(alias="Number of Medicare Beneficiaries")   
    number_of_distinct_medicare_beneficiary_per_day_services: Optional[int]= Field(alias="Number of Distinct Medicare Beneficiary Per Day Service")   
    average_Medicare_allowed_amount: Optional[float]= Field(alias="Average Medicare Allowed Amount")   
    average_submitted_charge_amount: Optional[float]= Field(alias="Average Medicare Submitted Charge Amount")   
    average_medicare_payment_amount: Optional[float]= Field(alias="Average Medicare Payment Amount")   
    average_medicare_standardized_amount: Optional[float]= Field(alias="Average Medicare Standardized Amount")   

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        validate_all = True


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
    medicaredata: List[MedicareData]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        validate_all = True

