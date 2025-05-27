from pydantic_settings import BaseSettings
from functools import lru_cache
import os
import json
from typing import List

class Settings(BaseSettings):
    DEBUG: bool = os.getenv("DEBUG")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_URL_PRODUCCION: str = os.getenv("DATABASE_URL_PRODUCCION")

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()