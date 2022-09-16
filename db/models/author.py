from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship

from db.base_class import Base


class Autor(Base):
    id = Column(Integer, primary_key = True, index = True)
    nombre = Column(String, nullable = False)    