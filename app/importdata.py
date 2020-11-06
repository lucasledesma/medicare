import sqlite3 as sql
from typing import Counter
import pandas as pd
import sys
import os.path

environments = ['development', 'test', 'production']
environment = os.environ.get('ENV')

if not environment in environments: 
    print("Invalid environment. Defaulting to 'development' ")    
    os.environ["ENV"] = "development"
    environment ='development'

databasename = "./data/" + environment + ".db"
nrows=None if environment == 'production' else 1000 
print("Environment: ", environment)  
print("Databasename: ", databasename)  
print("Number of rows=: ", nrows)  

conn = sql.connect(databasename)

cursor = conn.cursor()

cursor.execute("create table if not exists migrations (id integer primary key, description text);")
cursor.execute("select * from migrations")
print("Migrations already in the db: ", cursor.fetchall())
cursor.execute("select COALESCE(MAX(id), 0) from migrations")
migration_nro = cursor.fetchone()[0]

if migration_nro < 1 :
    print("MIGRATION 1: Inserting csv data into tmp table... ")
    medicaredata = pd.read_csv("./data/data.csv",nrows=nrows)
    cursor.execute("drop table if exists tmp;")
    medicaredata.to_sql('tmp', conn)
    cursor.execute("insert into migrations(id, description) values (1, 'Inserting csv data into tmp table');")
    conn.commit()
    print("MIGRATION 1: Done")    

if migration_nro < 2: 
    print("MIGRATION 2: Creating table providers... ")
    cursor.execute("""create table if not exists providers 
                        (
                            id INTEGER PRIMARY KEY, 
                            lastname TEXT, 
                            firstname TEXT, 
                            middle_initial TEXT,
                            credentials TEXT,
                            gender TEXT,
                            entity_type TEXT,
                            street_address_1 TEXT,
                            street_address_2 TEXT,
                            city TEXT,
                            zip_code TEXT,
                            state_code TEXT,
                            country_code TEXT,
                            provider_type TEXT
                        );""")
    cursor.execute("insert into migrations(id, description) values (2, 'Creating table providers... ');")
    conn.commit()
    print("MIGRATION 2: Done")    

if migration_nro < 3: 
    print("MIGRATION 3: Creating table medicare_data... ")
    cursor.execute("""create table if not exists medicare_data 
                    (
                        id  INTEGER PRIMARY KEY AUTOINCREMENT,
                        provider_id INTEGER,
                        medicare_participation_indicator TEXT,
                        place_of_service TEXT,
                        hcpcs_code TEXT,
                        hcpcs_description TEXT,
                        hcpcs_drug_indicator TEXT,
                        number_of_services INTEGER,
                        number_of_medicare_beneficiaries INTEGER,
                        number_of_distinct_medicare_beneficiary_per_day_services INTEGER,
                        average_Medicare_allowed_amount FLOAT,
                        average_submitted_charge_amount FLOAT,
                        average_medicare_payment_amount FLOAT,
                        average_medicare_standardized_amount FLOAT,
                        FOREIGN KEY(provider_id) references providers(id) 
                    );""")
    cursor.execute("insert into migrations(id, description) values (3, 'Creating table medicare... ');")
    conn.commit()
    print("MIGRATION 3: Done")    

if migration_nro < 4: 
    print("MIGRATION 4: Populating providers table... ")
    cursor.execute("""insert into providers 
                        select distinct  
                            "National Provider Identifier",
                            COALESCE("Last Name/Organization Name of the Provider",""),
                            COALESCE("First Name of the Provider",""),
                            COALESCE("Middle Initial of the Provider",""),
                            COALESCE("Credentials of the Provider",""),
                            COALESCE("Gender of the Provider",""),
                            COALESCE("Entity Type of the Provider",""),
                            COALESCE("Street Address 1 of the Provider",""),
                            COALESCE("Street Address 2 of the Provider",""),
                            COALESCE("City of the Provider",""),
                            printf("%09d","Zip Code of the Provider"),
                            "State Code of the Provider",
                            "Country Code of the Provider",
                            "Provider Type"
                        from tmp;""")

    cursor.execute("insert into migrations(id, description) values (4, 'Populating providers table... ');")
    conn.commit()
    print("MIGRATION 4: Done")  

if migration_nro < 5: 
    print("MIGRATION 5: Populating medicare_data table... ")
    cursor.execute("""insert into medicare_data
                        select 
                            null,
                            "National Provider Identifier",                        
                            "Medicare Participation Indicator",
                            "Place of Service",
                            "HCPCS Code",
                            "HCPCS Description" ,
                            "HCPCS Drug Indicator",
                            "Number of Services",
                            "Number of Medicare Beneficiaries",
                            "Number of Distinct Medicare Beneficiary/Per Day Services",
                            "Average Medicare Allowed Amount",
                            "Average Submitted Charge Amount",
                            "Average Medicare Payment Amount",
                            "Average Medicare Standardized Amount"                        
                        from tmp;""")

    cursor.execute("insert into migrations(id, description) values (5, 'Populating medicare_data table... ');")
    conn.commit()
    print("MIGRATION 5: Done")  

if migration_nro < 6: 
    print("MIGRATION 6: Creating indexes... ")
    cursor.execute("CREATE INDEX IF NOT EXISTS medicare_provider_id ON medicare_data(provider_id)");
    cursor.execute("CREATE INDEX IF NOT EXISTS providers_id ON providers(id)");
    cursor.execute("CREATE INDEX IF NOT EXISTS providers_name ON providers(firstname,lastname)");
    cursor.execute("CREATE INDEX IF NOT EXISTS medicaredata_provider_hcpcs_code ON medicare_data(provider_id,hcpcs_code)");
    cursor.execute("insert into migrations(id, description) values (6, 'Creating indexes... ');")
    conn.commit()
    print("MIGRATION 6: Done")  

if migration_nro < 7: 
    print("Cleaning up... ")
    cursor.execute("drop table if exists tmp;")
    cursor.execute("vacuum;")
    cursor.execute("insert into migrations(id, description) values (7, 'Cleaning up... ');")
    conn.commit()
    print("MIGRATION 7: Done")  

cursor.close()