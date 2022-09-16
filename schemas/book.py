from datetime import date
from pydantic import BaseModel

from core.enums.enums import Formato, Idioma

class BookCreate(BaseModel):
    titulo: str
    precio: float | None
    propietario: str
    isbn: str | None
    sinopsis: str | None
    imagen: str | None
    editorial: str | None
    fecha_compra: date | None
    observaciones: str | None
    categoria: str | None
    formato: Formato
    idioma: Idioma
    saga: str | None
    valoracion: int | None
    fecha_inicio_lectura: date | None
    fecha_fin_lectura: date | None

class BookShow(BaseModel) :
    id: int
    titulo : str 

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
