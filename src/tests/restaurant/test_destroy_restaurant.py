from tests.base import client
from uuid import uuid4

from .base import url, create


def test_destroy():
    data = create()
    response = client.delete(
        f"{url}/{data['id']}")
    assert response.status_code == 204


def test_destroy_not_found():
    response = client.delete(
        f"{url}/{uuid4()}")
    assert ('detail' in response.json()) == True
    assert response.status_code == 404
