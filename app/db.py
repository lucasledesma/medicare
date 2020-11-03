import databases
from sqlalchemy import Column, Integer, Table, MetaData, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import config

Base = declarative_base()
DATABASE_URL = config.get_settings().database_url
database = databases.Database(DATABASE_URL)
metadata = MetaData()

class ProviderTable(Base):
    __tablename__ = 'providers'
    id = Column(name="id", type_=Integer, primary_key=True)
    lastname = Column(name="lastname", type_=String)
    firstname = Column(name="firstname", type_=String)
    middle_initial = Column(name="middle_initial", type_=String)
    credentials = Column(name="credentials" , type_=String)
    gender = Column(name="gender" , type_=String)
    entity_type = Column(name="entity_type" , type_=String)
    street_address_1 = Column(name='street_address_1', type_=String)
    street_address_2 = Column(name="street_address_2" , type_=String)
    city = Column(name="city" , type_=String)
    zip_code = Column(name="zip_code" , type_=String)
    state_code = Column(name="state_code" , type_=String)
    country_code = Column(name="country_code" , type_=String)
    provider_type = Column(name="provider_type" , type_=String)
    medicaredata = relationship("MedicareDataTable")

class MedicareDataTable(Base):
    __tablename__ = 'medicare_data'
    id =  Column(name="id", type_=Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey(ProviderTable.id))
    medicare_participation_indicator = Column(name="medicare_participation_indicator", type_=String)    
    hcpcs_code = Column(name="hcpcs_code", type_=String)
    hcpcs_description = Column(name="hcpcs_description", type_= String)
    hcpcs_drug_indicator = Column(name="hcpcs_drug_indicator", type_=String)
    number_of_services= Column(name="number_of_services", type_=Integer)
    number_of_medicare_beneficiaries=Column(name="number_of_medicare_beneficiaries", type_=Integer)
    number_of_distinct_medicare_beneficiary_per_day_services=Column(name="number_of_distinct_medicare_beneficiary_per_day_services", type_=Integer)
    average_Medicare_allowed_amount = Column(name="average_Medicare_allowed_amount", type_=Float)
    average_submitted_charge_amount = Column(name="average_submitted_charge_amount", type_=Float)
    average_medicare_payment_amount = Column(name="average_medicare_payment_amount", type_=Float)
    average_medicare_standardized_amount = Column(name="average_medicare_standardized_amount", type_=Float)    

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
Session = sessionmaker(bind=engine)
