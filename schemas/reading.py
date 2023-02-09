from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

from schemas.author_and_book import BookResumeShow

class ReadingShowFromBook(BaseModel):
    lector: str
    valoracion: Optional[int]
    fecha_inicio: date
    fecha_fin: Optional[date]

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
        allow_population_by_field_name = True


class ReadingShow(ReadingShowFromBook):
    libro: BookResumeShow
