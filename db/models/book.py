from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from typing import List

from db.base_class import Base
from db.models.autor_libros import Autor_Libros
from db.models.reading import Lectura
from schemas.book import BookCreate

class Libro(Base):
    id = Column(Integer, primary_key = True, index = True)
    titulo = Column(String, nullable = False)
    precio = Column(Float)
    propietario = Column(String, nullable = False)
    isbn = Column(String)
    sinopsis = Column(String)
    imagen = Column(String)
    editorial = Column(String)
    fecha_compra = Column(Date)
    observaciones = Column(String)
    categoria = Column(String)
    formato = Column(String, nullable = False)
    idioma = Column(String, nullable = False)
    saga = Column(String)
    autores = relationship("Autor_Libros", back_populates="libro", cascade="save-update, merge, delete, delete-orphan")
    lecturas = relationship("Lectura", back_populates="libro", cascade="save-update, merge, delete, delete-orphan")

def libroFromBookCreate(book: BookCreate):
    libro = Libro(**book.dict(exclude={'autores'}))
    autores = []
    for autor in book.autores:
        autores.append(Autor_Libros(autor_id = autor.id))
    libro.autores = autores
    return libro
