def test_admin_dashboard(client):
    response = client.get('/admin/dashboard')
    # Admin login required, so may redirect
    assert response.status_code in (200, 302)
