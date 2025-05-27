from sqlalchemy import Column, Integer, String, Float, DateTime , Text
from datetime import datetime
from app.core.database import Base

class Cotizacion(Base):
    __tablename__ = "cotizaciones"

    id = Column(Integer, primary_key=True, index=True)
    numero_cotizacion = Column(String, unique=True, index=True)
    nombre_cliente = Column(String)
    email = Column(String)
    tipo_servicio = Column(String) 
    descripcion = Column(Text) 
    precio = Column(Float)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)