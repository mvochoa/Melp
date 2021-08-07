from tests.base import client
from uuid import uuid4

from .base import url, create


def test_show():
    data = create()
    response = client.get(
        f"{url}/{data['id']}")
    assert set(data) <= set(response.json())
    assert response.status_code == 200


def test_show_not_found():
    response = client.get(
        f"{url}/{uuid4()}")
    assert ('detail' in response.json()) == True
    assert response.status_code == 404
