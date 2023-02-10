from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

from schemas.author_and_book import BookResumeShow

class ReadingComun(BaseModel):
    valoracion: Optional[int]    
    fecha_fin: Optional[date]

class ReadingShowFromBook(ReadingComun):
    lector: str
    fecha_inicio: date

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
        allow_population_by_field_name = True

class ReadingShow(ReadingShowFromBook):
    id: int
    libro: BookResumeShow

class ReadingCreate(ReadingComun):
    lector: str
    fecha_inicio: date
    libro_id: int

class ReadingPatch(ReadingComun):
    fecha_inicio: Optional[date]
