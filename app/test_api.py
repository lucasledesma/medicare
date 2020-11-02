from fastapi.testclient import TestClient
from main import app
import logging

LOGGER = logging.getLogger(__name__)

client = TestClient(app)

def test_providers_get():
    response = client.get("/providers?skip=0&take=1")
    assert response.status_code == 200
    assert response.json() == [
                                    {
                                        "National Provider Identifier": 1003000126,
                                        "Last Name/Organization Name of the Provider": "ENKESHAFI",
                                        "First Name of the Provider": "ARDALAN",
                                        "Middle Initial of the Provider": "",
                                        "Credentials of the Provider": "M.D.",
                                        "Gender of the Provider": "M",
                                        "Entity Type of the Provider": "I",
                                        "Street Address 1 of the Provider": "900 SETON DR",
                                        "Street Address 2 of the Provider": "",
                                        "City of the Provider": "CUMBERLAND",
                                        "Zip Code of the Provider": "215021854",
                                        "State Code of the Provider": "MD",
                                        "Country Code of the Provider": "US",
                                        "Provider Type": "Internal Medicine",
                                        "Medicare Participation Indicator": "Y",
                                        'HCPCS Code': '99217'
                                    }
                                ]

def test_provider_get():
    response = client.get("/providers/1003000126?skip=0&take=1")
    assert response.status_code == 200
    LOGGER.info(response.json())
    # assert response.json() == {
    #                             "National Provider Identifier": 1003000126,
    #                             "Last Name/Organization Name of the Provider": "ENKESHAFI",
    #                             "First Name of the Provider": "ARDALAN",
    #                             "Middle Initial of the Provider": "",
    #                             "Credentials of the Provider": "M.D.",
    #                             "Gender of the Provider": "M",
    #                             "Entity Type of the Provider": "I",
    #                             "Street Address 1 of the Provider": "900 SETON DR",
    #                             "Street Address 2 of the Provider": "",
    #                             "City of the Provider": "CUMBERLAND",
    #                             "Zip Code of the Provider": "215021854",
    #                             "State Code of the Provider": "MD",
    #                             "Country Code of the Provider": "US",
    #                             "Provider Type": "Internal Medicine",
    #                             "Medicare Participation Indicator": "Y",
    #                             'HCPCS Code': '99217'
    #                         }
                                    
    