from pydantic import BaseSettings
from functools import lru_cache
import os,logging

logger = logging.getLogger("uvicorn.error")

environments = ['development', 'test', 'production']
environment = os.environ.get('ENV')
if not environment in environments: 
    logger.warning("Invalid environment. Defaulting to 'development' ")    
    os.environ["ENV"] = "development"
else:
    logger.info('%s %s',"Environment: ", os.environ["ENV"])

@lru_cache()
def get_settings():
    return Settings()

class Settings(BaseSettings):
    app_name: str = "Middlecare API"
    database_url: str 
    environment: str = os.environ.get('ENV')

    class Config:
        env_file = "./app/.env." + os.environ.get('ENV')