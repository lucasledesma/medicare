from fastapi.testclient import TestClient
from app import main
import logging
from test_data import provider_1003000126, provider_1003000407, provider_1003000142, provider_1003000134

LOGGER = logging.getLogger(__name__)

client = TestClient(main.app)

def test_get_first_provider():
    response = client.get("/providers?skip=0&take=1")
    assert response.status_code == 200
    assert response.json() == [ provider_1003000126 ]

def test_get_second_provider():
    response = client.get("/providers?skip=1&take=1")
    assert response.status_code == 200
    assert response.json() == [ provider_1003000134 ]    

def test_get_first_and_second_providers():
    response = client.get("/providers?skip=0&take=2")
    assert response.status_code == 200
    assert response.json() == [ provider_1003000126,provider_1003000134 ]  

def test_get_provider_1003000126():
    response = client.get("/providers/1003000126")
    assert response.status_code == 200
    LOGGER.info(response.json())
    assert response.json() == provider_1003000126

def test_get_provider_1003000407():
    response = client.get("/providers/1003000407")
    assert response.status_code == 200
    LOGGER.info(response.json())
    assert response.json() == provider_1003000407

def test_nonexistent_provider():
    response = client.get("/providers/1")
    assert response.status_code == 404
    LOGGER.info(response.json())
    assert response.json() == {'detail': 'Provider not found'}

def test_invalid_provider():
    response = client.get("/providers/aaass")
    assert response.status_code == 422
    LOGGER.info(response.json())
    assert response.json() == {'detail': [{'loc': ['path', 'provider_id'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]}