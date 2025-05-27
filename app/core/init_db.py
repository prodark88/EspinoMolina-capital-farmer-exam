from app.core.database import Base, engine

async def init_db():
    try:
        print("Inicializando la base de datos...")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Base de datos inicializada con éxito.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")