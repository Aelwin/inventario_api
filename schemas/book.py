from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

from core.enums.enums import Formato, Idioma
from .author_and_book import BookResumeShow, AuthorResumeShow

class BookBase(BookResumeShow):
    propietario: str
    formato: Formato
    idioma: Idioma

class BookCreate(BaseModel):
    titulo: str
    propietario: str
    formato: Formato
    idioma: Idioma
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

class BookShow(BookResumeShow):
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
    autores: List[AuthorResumeShow]
