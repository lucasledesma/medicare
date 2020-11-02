import databases
from sqlalchemy import Column, Integer, Table, MetaData, String
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()

DATABASE_URL = "sqlite:///../data/test.db"

database = databases.Database(DATABASE_URL)

metadata = MetaData()

providers = Table(
    "providers",
    metadata,
    Column(name="id", type_=Integer, primary_key=True),
    Column(name="lastname", type_=sqlalchemy.String),
    Column(name="firstname", type_=sqlalchemy.String),
    Column(name="middle_initial", type_=sqlalchemy.String),
    Column(name="credentials" , type_=sqlalchemy.String),
    Column(name="gender" , type_=sqlalchemy.String),
    Column(name="entity_type" , type_=sqlalchemy.String),
    Column(name='street_address_1', type_=sqlalchemy.String),
    Column(name="street_address_2" , type_=sqlalchemy.String),
    Column(name="city" , type_=sqlalchemy.String),
    Column(name="zip_code" , type_=sqlalchemy.String),
    Column(name="state_code" , type_=sqlalchemy.String),
    Column(name="country_code" , type_=sqlalchemy.String),
    Column(name="provider_type" , type_=sqlalchemy.String),
    Column(name="medicare_participation_indicator", type_=sqlalchemy.String),
    #Column(name="hcpcs_code", type_=sqlalchemy.String)

)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
