import databases
from sqlalchemy import Column, Integer, Table, MetaData, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DATABASE_URL = "sqlite:///../data/test.db"
database = databases.Database(DATABASE_URL)
metadata = MetaData()

class ProviderTable(Base):
    __tablename__ = 'providers'
    id = Column(name="id", type_=Integer, primary_key=True)
    lastname = Column(name="lastname", type_=sqlalchemy.String)
    firstname = Column(name="firstname", type_=sqlalchemy.String)
    middle_initial = Column(name="middle_initial", type_=sqlalchemy.String)
    credentials = Column(name="credentials" , type_=sqlalchemy.String)
    gender = Column(name="gender" , type_=sqlalchemy.String)
    entity_type = Column(name="entity_type" , type_=sqlalchemy.String)
    street_address_1 = Column(name='street_address_1', type_=sqlalchemy.String)
    street_address_2 = Column(name="street_address_2" , type_=sqlalchemy.String)
    city = Column(name="city" , type_=sqlalchemy.String)
    zip_code = Column(name="zip_code" , type_=sqlalchemy.String)
    state_code = Column(name="state_code" , type_=sqlalchemy.String)
    country_code = Column(name="country_code" , type_=sqlalchemy.String)
    #provider_type = Column(name="provider_type" , type_=sqlalchemy.String)
    #medicare_participation_indicator = Column(name="medicare_participation_indicator", type_=sqlalchemy.String)
    #hcpcs_code = Column(name="hcpcs_code", type_=sqlalchemy.String)
    medicaredata = relationship("MedicareDataTable")

class MedicareDataTable(Base):
    __tablename__ = 'medicare_data'
    id =  Column(name="id", type_=Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey(ProviderTable.id))
    hcpcs_code = Column(name="hcpcs_code", type_=Integer)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
Session = sessionmaker(bind=engine)
