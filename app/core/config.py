from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite+aiosqlite:///./database.db"
    DATABASE_URL_PRODUCCION: str = "sqlite+aiosqlite:///./prod_database.db"

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()