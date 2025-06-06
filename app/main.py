from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import random
from app.core.init_db import init_db
from app.core.database import get_db
from app.models import Cotizacion
from app.schemas import CotizacionCreate, CotizacionResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
app = FastAPI()

#CONFIGURACION DE CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

settings = get_settings()  

#METODOS DE LA API
PRECIOS_SERVICIOS = {
    "Constitución de empresa": 1500,
    "Defensa laboral": 2000,
    "Consultoría tributaria": 800
}

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}


@app.post("/cotizar", response_model=CotizacionResponse)
async def generar_cotizacion(data: CotizacionCreate, db: AsyncSession = Depends(get_db)):
    if data.tipo_servicio not in PRECIOS_SERVICIOS:
        raise HTTPException(status_code=400, detail="Tipo de servicio inválido")

    numero = f"COT-2025-{random.randint(1000, 9999)}"
    cotizacion = Cotizacion(
        numero_cotizacion=numero,
        nombre_cliente=data.nombre_cliente,
        email=data.email,
        tipo_servicio=data.tipo_servicio,
        descripcion=data.descripcion,  # ← Aquí se agrega
        precio=PRECIOS_SERVICIOS[data.tipo_servicio],
        fecha_creacion=datetime.utcnow()
    )

    db.add(cotizacion)
    await db.commit()
    await db.refresh(cotizacion)

    return cotizacion


# Initialize database connection
@app.on_event("startup")
async def startup_event():
    await init_db()