import json
from core.enums.enums import Formato, Idioma

book = {
    "titulo": "El camino de los reyes",
    "propietario": "Juan",
    "formato": Formato.FISICO,
    "idioma": Idioma.CASTELLANO,
    "precio": 29.95,
    "editorial": "NOVA"
}

def test_create_book(client):
    data = book
    response = client.post("/libros/", json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["id"] == 1
    assert response.json()["titulo"] == book["titulo"]

def test_create_book_missing_required_property(client) :
    data = {}
    response = client.post("/libros/", json.dumps(data))
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"

def test_get_book_by_id(client) :
    response = client.get("/libros/1") # Recuperamos el libro creado en el primer test
    assert response.status_code == 200
    assert response.json()["titulo"] == book["titulo"]

def test_get_book_by_id_not_exist(client) :
    id = 999
    response = client.get(f"/libros/{id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"No existe ningún libro con el id {id}"

def test_get_all_books(client) :
    response = client.get("/libros/")
    assert response.status_code == 200
    assert len(response.json()) == 1 # Sólo estoy creando un Libro en estos test
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["titulo"] == book["titulo"]