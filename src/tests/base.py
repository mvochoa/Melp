from fastapi.testclient import TestClient
from faker import Faker
from faker.providers import python, company, internet, phone_number, address

from main import app

client = TestClient(app)
fake = Faker('es_MX')
fake.add_provider(python)
fake.add_provider(company)
fake.add_provider(internet)
fake.add_provider(phone_number)
fake.add_provider(address)
