from enum import Enum
from pydantic import BaseModel, EmailStr
from datetime import datetime

class TipoServicioEnum(str, Enum):
    constitucion = "Constitución de empresa"
    defensa = "Defensa laboral"
    consultoria = "Consultoría tributaria"

class CotizacionCreate(BaseModel):
    nombre_cliente: str
    email: EmailStr
    tipo_servicio: TipoServicioEnum
    descripcion: str

class CotizacionResponse(CotizacionCreate):
    numero_cotizacion: str
    precio: float
    fecha_creacion: datetime

    class Config:
        orm_mode = True