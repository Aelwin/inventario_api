from typing import List
from pydantic import BaseModel, Field

from .author_and_book import AuthorResumeShow, BookResumeShow

class AuthorCreate(BaseModel):
    nombre: str

class AuthorShow(AuthorResumeShow):
    libros: List[BookResumeShow] 