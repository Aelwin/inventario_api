from pydantic import BaseModel, Field

class BookResumeShow(BaseModel):
    id: int = Field(alias="libro_id")
    titulo: str = Field(alias="libro_titulo")

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
        allow_population_by_field_name = True

class AuthorResumeShow(BaseModel):
    id: int = Field(alias='autor_id')
    nombre: str = Field(alias='autor_nombre')

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
        allow_population_by_field_name = True
