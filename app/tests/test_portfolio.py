def test_portfolio_route(client):
    response = client.get('/portfolio')
    assert response.status_code == 200
    assert b"My Projects" in response.data