from http.client import HTTPException
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from schemas.book import BookCreate, BookShow
from db.repository.book import crearLibro, recuperarLibro, recuperarLibros, actualizarLibro, eliminarLibro

router = APIRouter()

def notFoundException(id):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Libro con id {id} no encontrado")

@router.post("/", status_code = status.HTTP_201_CREATED)
def crear_libro(libro: BookCreate, db: Session = Depends(get_db)):
    libro = crearLibro(libro, db)
    return libro

@router.get("/{libro_id}", response_model = BookShow, response_model_by_alias=False)
def recuperar_libro(libro_id : int, db: Session = Depends(get_db)):
    libro = recuperarLibro(libro_id, db)
    if not libro:
        raise notFoundException(libro_id)
    return libro

@router.get("/", response_model = List[BookShow], response_model_by_alias=False)
def recuperar_libros(db: Session = Depends(get_db)):
    return recuperarLibros(db)

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