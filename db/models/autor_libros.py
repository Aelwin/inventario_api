from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from db.base_class import Base

class Autor_Libros(Base):    
    libro_id = Column(ForeignKey('books.id'), primary_key=True)
    autor_id = Column(ForeignKey('authors.id'), primary_key=True)
    #libro = relationship("Libro", back_populates="autores")
    #autor = relationship("Autor", back_populates="libros")

    #proxies
    #id = association_proxy(target_collection='autor', attr='id')
    #nombre = association_proxy(target_collection='autor', attr='nombre')
    #book_title = association_proxy(target_collection='book', attr='title')