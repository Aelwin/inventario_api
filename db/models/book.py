from email.policy import default
from sqlalchemy import Column, Integer, String, Float, Date

from db.base_class import Base

class Libro(Base):
    id = Column(Integer, primary_key = True, index = True)
    titulo = Column(String, nullable = False)
    precio = Column(Float)
    propietario = Column(String, nullable = False)
    isbn = Column(String)
    sinopsis = Column(String)
    imagen = Column(String)
    editorial = Column(String)
    fecha_compra = Column(Date)
    observaciones = Column(String)
    categoria = Column(String)
    formato = Column(String, nullable = False)
    idioma = Column(String, nullable = False)
    saga = Column(String)
    valoracion = Column(Integer)
    fecha_inicio_lectura = Column(Date)
    fecha_fin_lectura = Column(Date)

