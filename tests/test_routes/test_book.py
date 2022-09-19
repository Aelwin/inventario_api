import json
from core.enums.enums import Formato, Idioma
from fastapi import status

book = {
    "titulo": "El camino de los reyes",
    "propietario": "Juan",
    "formato": Formato.FISICO,
    "idioma": Idioma.CASTELLANO,
    "precio": 29.95,
    "editorial": "NOVA"
}

ruta_libros = "/libros"
ruta_crear = "/crear"
ruta_actualizar = "/actualizar"
ruta_eliminar = "/eliminar"

def test_create_book(client):
    data = book
    response = client.post(f"{ruta_libros}{ruta_crear}/", json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["id"] == 1
    assert response.json()["titulo"] == book["titulo"]

def test_create_book_missing_required_property(client) :
    data = {}
    response = client.post(f"{ruta_libros}{ruta_crear}/", json.dumps(data))
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"

def test_get_book_by_id(client) :
    response = client.get(f"{ruta_libros}/1") # Recuperamos el libro creado en el primer test
    assert response.status_code == 200
    assert response.json()["titulo"] == book["titulo"]

def test_get_book_by_id_not_exist(client) :
    id = 999
    response = client.get(f"{ruta_libros}/{id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"No existe ningún libro con el id {id}"

def test_get_all_books(client) :
    response = client.get("/libros/")
    assert response.status_code == 200
    assert len(response.json()) == 1 # Sólo estoy creando un Libro en estos test
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["titulo"] == book["titulo"]

def test_update_book(client) :
    data = book
    data["titulo"] = "Otro titulo"
    response = client.put(f"{ruta_libros}{ruta_actualizar}/1", json.dumps(data))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["msg"] == "Libro actualizado correctamente."

def test_delete_book(client) :
    response = client.delete(f"{ruta_libros}{ruta_eliminar}/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["msg"] == "Libro eliminado correctamente."
    response = client.get(f"{ruta_libros}/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND