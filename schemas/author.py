from pydantic import BaseModel

class AuthorCreate(BaseModel):
    nombre: str

class AuthorShow(BaseModel):
    id: int
    nombre : str 

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True