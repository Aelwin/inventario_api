from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base
from db.models.autor_libros import Autor_Libros

class Autor(Base):
    id = Column(Integer, primary_key = True, index = True)
    nombre = Column(String, nullable = False)
    libros = relationship("Autor_Libros", back_populates="autor")