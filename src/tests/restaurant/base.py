from tests.base import fake

from database.connection import SessionLocal
from models.restaurant_model import RestaurantModel

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


def create(new_data={}):
    restaurant = RestaurantModel(**{**data, **new_data})
    db = SessionLocal()
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    db.close()
    return restaurant.dict()


def destroy(id):
    db = SessionLocal()
    restaurant = RestaurantModel.find(id, db)
    restaurant.delete()
    db.commit()
    db.close()
