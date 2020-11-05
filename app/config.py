from pydantic import BaseSettings
from functools import lru_cache
import os,logging

logger = logging.getLogger("uvicorn.error")

environments = ['development', 'test', 'production']
environment = os.environ.get('ENV')
if not environment in environments: 
    logger.warning("Invalid environment. Defaulting to 'development' ")    
    os.environ["ENV"] = "development"

@lru_cache()
def get_settings():
    return Settings()

class Settings(BaseSettings):
    app_name: str = "Middlecare API"
    database_url: str 

    class Config:
        env_file = ".env." + os.environ.get('ENV')