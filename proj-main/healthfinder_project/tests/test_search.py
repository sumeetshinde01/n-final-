def test_search_route(client):
    response = client.get('/search/')
    assert response.status_code == 200
    assert b"Search" in response.data
