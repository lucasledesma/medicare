from pydantic import BaseSettings
from functools import lru_cache

@lru_cache()
def get_settings():
    return Settings()

class Settings(BaseSettings):
    app_name: str = "Middlecare API"
    database_url: str = "sqlite:///../data/test.db"

    class Config:
        env_file = ".env"