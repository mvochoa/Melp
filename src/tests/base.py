from fastapi.testclient import TestClient
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()
