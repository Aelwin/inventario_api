import json
from fastapi import status

from core.enums.enums import Formato, Idioma
from core.config import settings
from test_author import test_create_author

book = {
    "titulo": "El camino de los reyes",
    "propietario": "Juan",
    "formato": Formato.FISICO,
    "idioma": Idioma.CASTELLANO,
    "precio": 29.95,
    "editorial": "NOVA",
    "autores": [
        {
            "autor_id": 1,
            "autor_nombre": "string"
        }
    ]
}

def test_create_book(client):
    test_create_author(client)
    data = book
    response = client.post(f"{settings.RUTA_LIBROS}/", json.dumps(data))
    assert response.status_code == status.HTTP_201_CREATED 
    assert response.json()["id"] == 1
    assert response.json()["titulo"] == book["titulo"]

def test_create_book_missing_required_property(client) :
    data = {}
    response = client.post(f"{settings.RUTA_LIBROS}/", json.dumps(data))
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"

def test_get_book_by_id(client) :
    response = client.get(f"{settings.RUTA_LIBROS}/1") # Recuperamos el libro creado en el primer test
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["titulo"] == book["titulo"]

def test_get_book_by_id_not_exist(client) :
    id = 999
    response = client.get(f"{settings.RUTA_LIBROS}/{id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == f"Libro con id {id} no encontrado"

def test_get_all_books(client) :
    response = client.get("/libros/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1 # Sólo estoy creando un Libro en estos test
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["titulo"] == book["titulo"]

"""def test_update_book(client) :
    data = book
    data["titulo"] = "Otro titulo"
    response = client.put(f"{settings.RUTA_LIBROS}/1", json.dumps(data))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["titulo"] == "Otro titulo"
    """

def test_delete_book(client) :
    response = client.delete(f"{settings.RUTA_LIBROS}/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    response = client.get(f"{settings.RUTA_LIBROS}/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND