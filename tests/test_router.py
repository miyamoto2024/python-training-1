from fastapi.testclient import TestClient
from app.router import app

client = TestClient(app)

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_bye():
    response = client.get("/bye")
    assert response.status_code == 200
    assert response.json() == {"message": "Bye"}