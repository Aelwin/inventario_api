from sqlalchemy.orm import Session
from db.models.reading import Lectura
from schemas.reading import ReadingCreate, ReadingPatch

def recuperarLectura(lectura_id: int, db: Session):
    return db.query(Lectura).filter(Lectura.id == lectura_id).first()

def recuperarLecturas(db: Session):
    return db.query(Lectura).all()

def eliminarLectura(lectura_id: int, db: Session):
    existing_reading = db.query(Lectura).filter(Lectura.id == lectura_id)
    if not existing_reading.first():
        return 0    
    existing_reading.delete(synchronize_session=False)
    db.commit()
    return 1

def crearLectura(reading: ReadingCreate, db: Session):
    lectura = Lectura(**reading.dict())
    db.add(lectura)
    db.commit()
    db.refresh(lectura)
    return lectura

def actualizarLectura(lectura_id: int, reading: ReadingCreate, db: Session) :
    existing_reading = db.query(Lectura).filter(Lectura.id == lectura_id)
    if not existing_reading.first():
        return 0    
    existing_reading.update(reading.__dict__)
    db.commit()
    return 1

def actualizarLecturaParcial(lectura_id: int, reading: ReadingPatch, db: Session) :
    existing_reading = db.query(Lectura).filter(Lectura.id == lectura_id)
    if not existing_reading.first():
        return 0    
    existing_reading.update(reading.dict(exclude_unset=True))
    db.commit()
    return 1

def recuperarLecturasPorLibro(libro_id: int, db: Session):
    return db.query(Lectura).filter(Lectura.libro_id == libro_id).all()