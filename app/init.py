import sqlite3 as sql
from typing import Counter
import pandas as pd
import logging


def init_db():

    logger = logging.getLogger("uvicorn.error")

    conn = sql.connect('./data/medicare.db')

    cursor = conn.cursor()

    cursor.execute("create table if not exists migrations (id integer primary key, description text);")
    cursor.execute("select * from migrations")
    logger.info('%s %s',"Migrations already in the db:", cursor.fetchall())
    cursor.execute("select COALESCE(MAX(id), 0) from migrations")
    migration_nro = cursor.fetchone()[0]

    if migration_nro < 1 :
        logger.info("MIGRATION 1: Inserting csv data into tmp table... ")
        medicaredata = pd.read_csv(
            "./data/data.csv")
        medicaredata.to_sql('tmp', conn)
        cursor.execute("insert into migrations(id, description) values (1, 'Inserting csv data into tmp table');")
        conn.commit()
    logger.info("MIGRATION 1: Done")    

    if migration_nro < 2: 
        logger.info("MIGRATION 2: Creating table providers... ")
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
    logger.info("MIGRATION 2: Done")    

    if migration_nro < 3: 
        logger.info("MIGRATION 3: Creating table medicare_data... ")
        cursor.execute("""create table if not exists medicare_data 
                        (
                            id  INTEGER PRIMARY KEY AUTOINCREMENT,
                            provider_id INTEGER,
                            medicare_participation_indicator TEXT,
                            place_of_service TEXT,
                            hcpcs_code TEXT,
                            hcpcs_description TEXT,
                            hcpcs_drug_indicator TEXT,
                            number_of_services TEXT,
                            number_of_medicare_beneficiaries TEXT,
                            number_of_distinct_medicare_beneficiary_per_day_services TEXT,
                            average_Medicare_allowed_amount TEXT,
                            average_submitted_charge_amount TEXT,
                            average_medicare_payment_amount TEXT,
                            average_medicare_standardized_amount TEXT,
                            FOREIGN KEY(provider_id) references providers(id) 
                        );""")
        cursor.execute("insert into migrations(id, description) values (3, 'Creating table medicare... ');")
        conn.commit()
    logger.info("MIGRATION 3: Done")    

# elif numberOfRows == 9847443:
#     logger.info("Rows alreafy in tmp table. Row count:",  numberOfRows)
# else:
#     logger.info("Wrong number of rows in tmp table! Row count:",  numberOfRows)
#     logger.info("Please delete the db or truncate the table and try again.")
#     exit(1)


# logger.info("Creating table medicare_data...")


# logger.info("Inserting data into table providers...")
# cursor.execute("""insert into providers
#                     select distinct 
#                     "National Provider Identifier",
#                     "Last Name/Organization Name of the Provider", 
#                     "First Name of the Provider", 
#                     middle_initial,
#                     credentials ,
#                     gender ,
#                     entity_type ,
#                     street_address_1 ,
#                     street_address_2 ,
#                     city ,
#                     zip_code ,
#                     state_code ,
#                     country_code,
#                     provider_type 
#                     from tmp;"""
#                 )

# logger.info("Wait while creating indexes...")
# cursor.execute("CREATE INDEX medicare_provider_id ON medicare_data(provider_id)");
# cursor.execute("CREATE INDEX providers_id ON providers(id)");

# cursor.close()