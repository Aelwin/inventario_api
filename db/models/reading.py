from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Lectura(Base):
    id = Column(Integer, primary_key = True, index = True)
    lector = Column(String, nullable = False)
    fecha_inicio = Column(Date, nullable = False)
    fecha_fin = Column(Date)
    valoracion = Column(Integer)
    libro_id = Column(Integer, ForeignKey("libro.id"))
    libro = relationship("Libro", back_populates="lecturas")