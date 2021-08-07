from tests.base import client

from schemas.restaurant_schema import ResponseStatistics
from .base import url, create, destroy

url = f"{url}/statistics"


def test_statistics():
    # La distacia de (10.52, 10.52) de los siguientes restaurates es de 1560 metros
    restaurants = [create({'lng': 10.53, 'lat': 10.53, 'rating': 4}),
                   create({'lng': 10.51, 'lat': 10.51, 'rating': 3}),
                   create({'lng': 10.53, 'lat': 10.51, 'rating': 2}),
                   create({'lng': 10.52, 'lat': 10.53, 'rating': 1})]
    response = client.get(url, params={
                          'latitude': 10.52, 'longitude': 10.52, 'radius': 1600})
    for restaurant in restaurants:
        destroy(restaurant['id'])

    assert response.json() == ResponseStatistics(
        count=4, avg=2.5, std=1.2909944487358056).dict()
    assert response.status_code == 200


def test_statistics_not_found_restaurant():
    response = client.get(url, params={
                          'latitude': 0, 'longitude': 0, 'radius': 1})
    assert response.json() == ResponseStatistics(count=0, avg=None, std=None).dict()
    assert response.status_code == 200
