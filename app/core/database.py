from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool
from app.core.config import get_settings

settings = get_settings()

# Configuración de la base de datos
DATABASE_URL = settings.DATABASE_URL_PRODUCCION if not settings.DEBUG else settings.DATABASE_URL

engine = create_async_engine(
    DATABASE_URL, future=True, echo=True, poolclass=NullPool
)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

