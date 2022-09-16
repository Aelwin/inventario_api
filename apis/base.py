from fastapi import APIRouter

from apis.version1 import route_homepage, route_author, route_book

api_router = APIRouter()
api_router.include_router(route_homepage.router, prefix="", tags=["general_pages"])
api_router.include_router(route_author.router, prefix="/autores", tags=["autores"])
api_router.include_router(route_book.router, prefix="/libros", tags=["libros"])