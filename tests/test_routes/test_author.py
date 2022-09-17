import json
from fastapi import status

nombre = "Brandon Sanderson"
ruta_autores = "/autores"
ruta_crear = "/crear"
ruta_actualizar = "/actualizar"
ruta_eliminar = "/eliminar"

def test_create_author(client):    
    data = {"nombre": nombre}
    response = client.post(f"{ruta_autores}{ruta_crear}/", json.dumps(data))
    assert response.status_code == status.HTTP_200_OK 
    assert response.json()["nombre"] == nombre

def test_create_author_no_name(client) :
    data = {}
    response = client.post(f"{ruta_autores}{ruta_crear}/", json.dumps(data))
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"

def test_get_author_by_id(client) :
    response = client.get(f"{ruta_autores}/1") # Recuperamos el autor creado en el primer test
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["nombre"] == nombre

def test_get_author_by_id_not_exist(client) :
    id = 999
    response = client.get(f"{ruta_autores}/{id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == f"No existe ningún autor con el id {id}"

def test_get_all_authors(client) :
    response = client.get(f"{ruta_autores}/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1 # Sólo estoy creando un Autor en estos test
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["nombre"] == nombre

def test_update_author(client) :
    data = {"nombre": "Otro nombre"}
    response = client.put(f"{ruta_autores}{ruta_actualizar}/1", json.dumps(data))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["msg"] == "Autor actualizado correctamente."

def test_delete_author(client) :
    response = client.delete(f"{ruta_autores}{ruta_eliminar}/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["msg"] == "Autor eliminado correctamente."
    response = client.get(f"{ruta_autores}/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND

