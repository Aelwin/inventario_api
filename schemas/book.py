from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from core.enums.enums import Formato, Idioma
from schemas.author import AuthorShow

class BookBase(BaseModel) :
    titulo: str
    propietario: str
    formato: Formato
    idioma: Idioma
    autores: List[AuthorShow]

class BookCreate(BookBase):
    precio: float | None
    isbn: str | None
    sinopsis: str | None
    imagen: str | None
    editorial: str | None
    fecha_compra: date | None
    observaciones: str | None
    categoria: str | None
    saga: str | None
    valoracion: int | None
    fecha_inicio_lectura: date | None
    fecha_fin_lectura: date | None

class BookShow(BookBase) :
    id: int    
    precio: Optional[float]   
    isbn: Optional[str]
    sinopsis: Optional[str]
    imagen: Optional[str]
    editorial: Optional[str]
    fecha_compra: Optional[date]
    observaciones: Optional[str]
    categoria: Optional[str]
    saga: Optional[str]
    valoracion: Optional[int]
    fecha_inicio_lectura: Optional[date]
    fecha_fin_lectura: Optional[date]

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
        allow_population_by_field_name = True

class BookResumeShow(BaseModel):
    id: int
    titulo: str
