import os
from tests.base import client

url = "/"


def test_main():
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == {
        "commit": os.environ.get('VERSION', ''),
        "github": "https://github.com/mvochoa/melp"
    }
