from fastapi.testclient import TestClient
from app import main
import logging
from test_data import provider_1003000126, provider_1003000407, provider_1003000134
import json

client = TestClient(main.app)

def test_get_skip_0_take_1_provider():
    response = client.get("/providers?skip=0&take=1")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_skip_1_take_1_provider():
    response = client.get("/providers?skip=1&take=1")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_skip_0_take_2_providers():
    response = client.get("/providers?skip=0&take=2")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_skip_1_take_2_providers():
    response = client.get("/providers?skip=1&take=2")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_lastname_contains_A_providers():
    response = client.get("/providers?skip=0&take=20&lastname=A")
    assert response.status_code == 200
    for provider in json.loads(response.text):
        assert provider["Last Name/Organization Name of the Provider"].find("A") > -1

def test_get_firstname_contains_B_providers():
    response = client.get("/providers?skip=0&take=20&firstname=B")
    assert response.status_code == 200
    for provider in json.loads(response.text):
        assert provider["First Name of the Provider"].find("B") > -1

def test_get_lastname_and_firstname_contain_A_providers():
    response = client.get("/providers?skip=0&take=20&lastname=A&firstname=A")
    assert response.status_code == 200
    for provider in json.loads(response.text):
        assert provider["Last Name/Organization Name of the Provider"].find("A") > -1
        assert provider["First Name of the Provider"].find("A") > -1

def test_get_hcpcs_code():
    response = client.get("/providers?skip=0&take=20&hcpcs_code=64491")
    assert response.status_code == 200
    for provider in json.loads(response.text):
        correct_code = False
        for record in provider["medicaredata"]:
            print(provider["First Name of the Provider"],record["Hcpcs code"])
            if record["Hcpcs code"]=="64491":
                correct_code = True
        assert correct_code == True  

def test_get_provider_1003000126():
    response = client.get("/providers/1003000126")
    assert response.status_code == 200
    assert response.json() == provider_1003000126

def test_get_provider_1003000407():
    response = client.get("/providers/1003000407")
    assert response.status_code == 200
    assert response.json() == provider_1003000407

def test_nonexistent_provider():
    response = client.get("/providers/1")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Provider not found'}

def test_invalid_provider():
    response = client.get("/providers/aaass")
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['path', 'provider_id'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]}