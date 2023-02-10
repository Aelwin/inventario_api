from fastapi import APIRouter, HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from schemas.reading import *
from db.repository.reading import *

router = APIRouter()

def notFoundException(propiedad: str, valor: str):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lectura con {propiedad} '{valor}' no encontrada")

@router.post("/", status_code = status.HTTP_201_CREATED)
def crear_lectura(lectura: ReadingCreate, db: Session = Depends(get_db)):
    lectura = crearLectura(lectura, db)
    return lectura

@router.get("/{lectura_id}", response_model = ReadingShow, response_model_by_alias=False)
def recuperar_lectura(lectura_id : int, db: Session = Depends(get_db)) :
    lectura = recuperarLectura(lectura_id, db)
    if not lectura:
        raise notFoundException('id', lectura_id)
    return lectura

@router.get("/", response_model = List[ReadingShow], response_model_by_alias=False)
def recuperar_lecturas(db: Session = Depends(get_db)) :
    return recuperarLecturas(db)

@router.put("/{lectura_id}", response_model = ReadingShow)
def actualizar_lectura(lectura_id: int, lectura: ReadingCreate, db: Session = Depends(get_db)) :
    message = actualizarLectura(lectura_id, lectura, db)
    if not message:
        raise notFoundException('id', lectura_id)
    return recuperarLectura(lectura_id, db)

@router.patch("/{lectura_id}", response_model = ReadingShow)
def actualizar_lectura_parcial(lectura_id: int, lectura: ReadingPatch, db: Session = Depends(get_db)) :
    message = actualizarLecturaParcial(lectura_id, lectura, db)
    if not message:
        raise notFoundException('id', lectura_id)
    return recuperarLectura(lectura_id, db)

@router.delete("/{lectura_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_autor(lectura_id: int, db: Session = Depends(get_db)) :
    message = eliminarLectura(lectura_id, db)
    if not message:
        raise notFoundException('id', lectura_id)