import json
import pytest
from src import app as flask_app

@pytest.fixture
def client():
    flask_app.app.testing = True
    with flask_app.app.test_client() as client:
        # reset state before each test
        client.post("/_test/reset")
        yield client

def test_create_and_list(client):
    r = client.post("/tasks", json={"title":"Tarefa 1", "description":"desc"})
    assert r.status_code == 201
    data = r.get_json()
    assert data["id"] == 1
    r2 = client.get("/tasks")
    assert r2.status_code == 200
    lst = r2.get_json()
    assert len(lst) == 1
    assert lst[0]["title"] == "Tarefa 1"

def test_get_not_found(client):
    r = client.get("/tasks/99")
    assert r.status_code == 404

def test_update_task(client):
    client.post("/tasks", json={"title":"T1"})
    r = client.put("/tasks/1", json={"title":"T1 edit", "done": True})
    assert r.status_code == 200
    data = r.get_json()
    assert data["title"] == "T1 edit"
    assert data["done"] == True

def test_delete_task(client):
    client.post("/tasks", json={"title":"T1"})
    r = client.delete("/tasks/1")
    assert r.status_code == 200
    r2 = client.get("/tasks")
    assert r2.get_json() == []
