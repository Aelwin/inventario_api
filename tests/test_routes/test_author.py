import json

def test_create_author(client):
    nombre = "Brandon Sanderson"
    data = {"nombre": nombre}
    response = client.post("/autores/", json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["nombre"] == nombre
    