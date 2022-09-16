from sqlalchemy.orm import Session
from schemas.author import AuthorCreate
from db.models.author import Autor

def crearAutor(autor: AuthorCreate, db: Session):
    autor = Autor(nombre = autor.nombre)
    db.add(autor)
    db.commit()
    db.refresh(autor)
    return autor

def recuperarAutor(autor_id: int, db: Session) :
    return db.query(Autor).filter(Autor.id == autor_id).first()

def recuperarAutores(db: Session) :
    return db.query(Autor).all()