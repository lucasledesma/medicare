from fastapi.testclient import TestClient
from app import main
import logging
from test_data import provider_1003000126

LOGGER = logging.getLogger(__name__)

client = TestClient(main.app)

def test_providers_get():
    response = client.get("/providers?skip=0&take=1")
    assert response.status_code == 200
    assert response.json() == [ provider_1003000126 ]

def test_provider_get():
    response = client.get("/providers/1003000126")
    assert response.status_code == 200
    LOGGER.info(response.json())
    assert response.json() == provider_1003000126