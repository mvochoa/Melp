from tests.base import client

from .base import url, data


def test_create():
    response = client.post(url, json=data)
    assert set(data) <= set(response.json())
    assert response.status_code == 201


def test_create_rating_out_range():
    response = client.post(url, json={**data, 'rating': 5})
    assert ('detail' in response.json()) == True
    assert response.status_code == 422


def test_create_phone_invalid():
    response = client.post(url, json={**data, 'phone': '3-12-39-8'})
    assert ('detail' in response.json()) == True
    assert response.status_code == 422
