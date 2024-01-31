from flask import json

from app import app
from unittest.mock import patch, Mock


def test_get_horoscope(client):
    # Test for a valid sign
    response = client.get('/get_horoscope?sign=virgo')
    assert response.status_code == 200
    data = response.get_json()
    assert 'daily' in data
    assert 'love' in data
    # ... assert other keys ...

    # Test for an invalid or missing sign
    response = client.get('/get_horoscope?sign=invalidsign')
    assert response.status_code == 400 or 404  # Depending on your implementation