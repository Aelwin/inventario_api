from fastapi import APIRouter, HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from schemas.author import AuthorCreate, AuthorShow
from db.repository.author import crearAutor, recuperarAutor, recuperarAutores, actualizarAutor, eliminarAutor

router = APIRouter()

def notFoundException(id):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Autor con id {id} no encontrado")

@router.post("/", status_code = status.HTTP_201_CREATED)
def crear_autor(autor: AuthorCreate, db: Session = Depends(get_db)):
    autor = crearAutor(autor, db)
    return autor

@router.get("/{autor_id}", response_model = AuthorShow, response_model_by_alias=False)
def recuperar_autor(autor_id : int, db: Session = Depends(get_db)) :
    autor = recuperarAutor(autor_id, db)
    if not autor:
        raise notFoundException(autor_id)
    return autor

@router.get("/", response_model = List[AuthorShow], response_model_by_alias=False)
def recuperar_autores(db: Session = Depends(get_db)) :
    return recuperarAutores(db)

@router.put("/{autor_id}")
def actualizar_autor(autor_id: int, autor: AuthorCreate, db: Session = Depends(get_db)) :
    message = actualizarAutor(autor_id, autor, db)
    if not message:
        raise notFoundException(autor_id)
    return recuperarAutor(autor_id, db)

@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_autor(autor_id: int, db: Session = Depends(get_db)) :
    message = eliminarAutor(autor_id, db)
    if not message:
        raise notFoundException(autor_id)