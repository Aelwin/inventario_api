from http.client import HTTPException
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from schemas.book import BookCreate, BookShow
from db.repository.book import crearLibro, recuperarLibro, recuperarLibros

router = APIRouter()

@router.post("/")
def crear_libro(libro: BookCreate, db: Session = Depends(get_db)):
    libro = crearLibro(libro = libro, db = db)
    return libro

@router.get("/{libro_id}", response_model = BookShow)
def recuperar_libro(libro_id : int, db: Session = Depends(get_db)) :
    libro = recuperarLibro(libro_id, db)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe ningún libro con el id {libro_id}")
    return libro

@router.get("/", response_model = List[BookShow])
def recuperar_libros(db: Session = Depends(get_db)) :
    return recuperarLibros(db)