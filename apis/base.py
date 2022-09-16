from fastapi import APIRouter

from apis.version1 import route_homepage
from apis.version1 import route_author

api_router = APIRouter()
api_router.include_router(route_homepage.router, prefix="", tags=["general_pages"])
api_router.include_router(route_author.router, prefix="/autores", tags=["autores"])