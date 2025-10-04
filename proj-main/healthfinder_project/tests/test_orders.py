def test_order_tracking_page(client):
    response = client.get('/order_tracking')
    assert response.status_code == 200
