from app import app


def test_about_page():
    with app.test_client() as test_client:
        response = test_client.get('/about')
        assert response.status_code == 200
        assert b"About Me" in response.data
        assert b"CoYo" in response.data  # Replace with actual content
