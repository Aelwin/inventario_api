from fastapi import APIRouter

from apis.version1 import route_homepage, route_author, route_book
from core.config import settings

api_router = APIRouter()
api_router.include_router(route_homepage.router, prefix="", tags=["general_pages"])
api_router.include_router(route_author.router, prefix=settings.RUTA_AUTORES, tags=["autores"])
api_router.include_router(route_book.router, prefix=settings.RUTA_LIBROS, tags=["libros"])