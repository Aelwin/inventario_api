from http.client import HTTPException
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from schemas.book import BookCreate, BookShow
from schemas.reading import ReadingShow
from db.repository.book import *
from db.repository.reading import recuperarLecturasPorLibro

router = APIRouter()

def notFoundException(propiedad: str, valor: str):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Libro con {propiedad} '{valor}' no encontrado")

@router.post("/", status_code = status.HTTP_201_CREATED)
def crear_libro(libro: BookCreate, db: Session = Depends(get_db)):
    libro = crearLibro(libro, db)
    return libro

@router.get("/{libro_id}", response_model = BookShow, response_model_by_alias=False)
def recuperar_libro(libro_id : int, db: Session = Depends(get_db)):
    libro = recuperarLibro(libro_id, db)
    if not libro:
        raise notFoundException('id', libro_id)
    return libro

@router.get("/", response_model = List[BookShow], response_model_by_alias=False)
def recuperar_libros(db: Session = Depends(get_db)):
    return recuperarLibros(db)

@router.get("/titulo/{libro_titulo}", response_model = List[BookShow], response_model_by_alias=False)
def recuperar_libros_titulo(libro_titulo : str, db: Session = Depends(get_db)) :
    libros = recuperarLibrosPorTitulo(libro_titulo, db)
    if not libros:
        raise notFoundException('titulo', libro_titulo)
    return libros

@router.put("/{libro_id}", response_model = BookShow)
def actualizar_libro(libro_id: int, book: BookCreate, db: Session = Depends(get_db)):
    message = actualizarLibro(libro_id, book, db)
    if not message:
        raise notFoundException(libro_id)
    return recuperarLibro(libro_id, db)

@router.delete("/{libro_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    message = eliminarLibro(libro_id, db)
    if not message:
        raise notFoundException(libro_id)

@router.get("/{libro_id}/lecturas", response_model= List[ReadingShow], response_model_by_alias=False)
def recuperar_lecturas(libro_id: int, db: Session = Depends(get_db)):
    lecturas = recuperarLecturasPorLibro(libro_id, db)
    if not lecturas:
        raise notFoundException('id', libro_id)    
    return lecturas