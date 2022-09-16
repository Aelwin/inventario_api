from fastapi import APIRouter, HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from schemas.author import AuthorCreate, AuthorShow
from db.session import get_db
from db.repository.author import crearAutor, recuperarAutor, recuperarAutores

router = APIRouter()

@router.post("/")
def crear_autor(autor: AuthorCreate, db: Session = Depends(get_db)):
    autor = crearAutor(autor = autor, db = db)
    return autor

@router.get("/{autor_id}", response_model = AuthorShow)
def recuperar_autor(autor_id : int, db: Session = Depends(get_db)) :
    autor = recuperarAutor(autor_id, db)
    if not autor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe ningún autor con el id {autor_id}")
    return autor

@router.get("/", response_model = List[AuthorShow])
def recuperar_autores(db: Session = Depends(get_db)) :
    return recuperarAutores(db)