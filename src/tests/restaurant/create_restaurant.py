from tests.base import client, fake

url = "/restaurants"
data = {
    'rating': fake.pyint(min_value=0, max_value=4),
    'name': fake.company(),
    'site': fake.url(),
    'email': fake.safe_email(),
    'phone': fake.msisdn(),
    'street': fake.street_address(),
    'city': fake.city(),
    'state': fake.country(),
    'lat': fake.pyfloat(min_value=-90, max_value=90),
    'lng': fake.pyfloat(min_value=-90, max_value=90),
}


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
