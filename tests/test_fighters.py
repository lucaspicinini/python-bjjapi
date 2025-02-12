

def test_fighters(client):
    response = client.get("/fighters", follow_redirects=True)
    assert 'application/json' in response.content_type
    assert response.status_code == 200

def test_fighters_pagination(client):
    response = client.get("/fighters", follow_redirects=True)
    per_page = len(response.get_json()['z_data'])
    current_page = response.get_json()['current_page']
    assert per_page == 30
    assert current_page == 1