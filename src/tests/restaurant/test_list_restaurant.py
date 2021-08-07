from tests.base import client

from .base import url


def test_list():
    response = client.get(url)
    assert isinstance(response.json(), list) == True
    assert response.status_code == 200
