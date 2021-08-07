from tests.base import client
from uuid import uuid4

from .base import url, data, create

restaurant = create()
url_id = f"{url}/{restaurant['id']}"


def test_update():
    response = client.put(url_id, json=data)
    assert set(data) <= set(response.json())
    assert response.status_code == 200


def test_update_not_found():
    response = client.put(
        f"{url}/{uuid4()}", json=data)
    assert ('detail' in response.json()) == True
    assert response.status_code == 404


def test_update_rating_out_range():
    response = client.put(url_id, json={**data, 'rating': 5})
    assert ('detail' in response.json()) == True
    assert response.status_code == 422


def test_update_phone_invalid():
    response = client.put(url_id, json={**data, 'phone': '3-12-39-8'})
    assert ('detail' in response.json()) == True
    assert response.status_code == 422
