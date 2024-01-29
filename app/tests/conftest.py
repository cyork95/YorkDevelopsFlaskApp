import pytest
from app import app


@pytest.fixture
def client():
    app.config.update({
        "TESTING": True,
        # Other configurations specific for testing
    })

    with app.test_client() as client:
        yield client
