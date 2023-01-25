import json
from fastapi import status

from core.config import settings

nombre = "Brandon Sanderson"

def test_create_author(client):    
    data = {"nombre": nombre}
    response = client.post(f"{settings.RUTA_AUTORES}/", json.dumps(data))
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["nombre"] == nombre

def test_create_author_no_name(client) :
    data = {}
    response = client.post(f"{settings.RUTA_AUTORES}/", json.dumps(data))
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"

def test_get_author_by_id(client) :
    response = client.get(f"{settings.RUTA_AUTORES}/1") # Recuperamos el autor creado en el primer test
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["nombre"] == nombre

def test_get_author_by_id_not_exist(client) :
    id = 999
    response = client.get(f"{settings.RUTA_AUTORES}/{id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == f"Autor con id {id} no encontrado"

def test_get_all_authors(client) :
    response = client.get(f"{settings.RUTA_AUTORES}/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1 # Sólo estoy creando un Autor en estos test
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["nombre"] == nombre

def test_update_author(client) :
    data = {"nombre": "Otro nombre"}
    response = client.put(f"{settings.RUTA_AUTORES}/1", json.dumps(data))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["nombre"] == "Otro nombre"

def test_delete_author(client) :
    response = client.delete(f"{settings.RUTA_AUTORES}/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    response = client.get(f"{settings.RUTA_AUTORES}/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND

