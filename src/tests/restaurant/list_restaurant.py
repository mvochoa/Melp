from tests.base import client

url = "/restaurants"


def test_list():
    response = client.get(url)
    assert isinstance(response.json(), list) == True
    assert response.status_code == 200
