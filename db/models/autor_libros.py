from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from db.base_class import Base

class Autor_Libros(Base):    
    libro_id = Column(ForeignKey('libro.id'), primary_key=True)
    autor_id = Column(ForeignKey('autor.id'), primary_key=True)
    libro = relationship("Libro", back_populates="autores")
    autor = relationship("Autor", back_populates="libros")

    #proxies    
    autor_nombre = association_proxy(target_collection='autor', attr='nombre')
    libro_titulo = association_proxy(target_collection='libro', attr='titulo')