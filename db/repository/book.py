from sqlalchemy.orm import Session

from db.models.book import Libro
from schemas.book import BookCreate

def crearLibro(libro: BookCreate, db: Session) :
    libro = Libro(**libro.dict())
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro

def recuperarLibro(id: int, db: Session):
    return db.query(Libro).filter(Libro.id == id).first()

def recuperarLibros(db: Session) :
    return db.query(Libro).all()