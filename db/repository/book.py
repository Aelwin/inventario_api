from sqlalchemy.orm import Session

from db.models.autor_libros import Autor_Libros
from db.models.book import Libro, libroFromBookCreate
from schemas.book import BookCreate

def crearLibro(libro: BookCreate, db: Session):
    libro = libroFromBookCreate(libro)
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro

def recuperarLibro(id: int, db: Session):
    return db.query(Libro).filter(Libro.id == id).first()

def recuperarLibros(db: Session):
    return db.query(Libro).all()

def recuperarLibrosPorTitulo(libro_titulo: str, db: Session):
    return db.query(Libro).filter(Libro.titulo.ilike(f"%{libro_titulo}%")).all()

def actualizarLibro(libro_id: int, libro: BookCreate, db: Session) :
    existing_book: Libro = recuperarLibro(libro_id, db)
    if not existing_book:
        return 0
    book_data = libro.dict(exclude={"autores"}, exclude_unset=True)
    for key, value in book_data.items():
        setattr(existing_book, key, value)
    autores = []
    for autor in libro.autores:
        autores.append(Autor_Libros(autor_id = autor.id))
    existing_book.autores = autores
    db.add(existing_book)
    db.commit()
    return 1

def eliminarLibro(libro_id: int, db: Session) :
    existing_book = db.query(Libro).filter(Libro.id == libro_id)
    if not existing_book.first():
        return 0
    existing_relation = db.query(Autor_Libros).filter(Autor_Libros.libro_id == libro_id)
    existing_relation.delete()
    existing_book.delete(synchronize_session=False)
    db.commit()
    return 1