from http.client import HTTPException
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from schemas.book import BookCreate, BookShow
from db.repository.book import crearLibro, recuperarLibro, recuperarLibros, actualizarLibro, eliminarLibro

router = APIRouter()

@router.post("/crear/")
def crear_libro(libro: BookCreate, db: Session = Depends(get_db)):
    libro = crearLibro(libro = libro, db = db)
    return libro

@router.get("/{libro_id}", response_model = BookShow, response_model_by_alias=False)
def recuperar_libro(libro_id : int, db: Session = Depends(get_db)) :
    libro = recuperarLibro(libro_id, db)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe ningún libro con el id {libro_id}")
    return libro

@router.get("/", response_model = List[BookShow], response_model_by_alias=False)
def recuperar_libros(db: Session = Depends(get_db)) :
    return recuperarLibros(db)

@router.put("/actualizar/{libro_id}")
def actualizar_libro(libro_id: int, book: BookCreate, db: Session = Depends(get_db)) :
    message = actualizarLibro(libro_id = libro_id, libro = book, db = db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con id {libro_id} no encontrado")
    return {"msg":"Libro actualizado correctamente."}

@router.delete("/eliminar/{libro_id}")
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)) :
    message = eliminarLibro(libro_id = libro_id, db = db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con id {libro_id} no encontrado")
    return {"msg":"Libro eliminado correctamente."}