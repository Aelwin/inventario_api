from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

from core.enums.enums import Formato, Idioma
from .reading import ReadingShowFromBook
from .author_and_book import *

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
    autores: List[AuthorFromBookCreate]

class BookShow(BookResumeShow):
    propietario: Optional[str]
    precio: Optional[float]   
    isbn: Optional[str]
    sinopsis: Optional[str]
    imagen: Optional[str]
    editorial: Optional[str]
    fecha_compra: Optional[date]
    observaciones: Optional[str]
    categoria: Optional[str]
    saga: Optional[str]
    autores: List[AuthorResumeShow]
    lecturas: List[ReadingShowFromBook]
