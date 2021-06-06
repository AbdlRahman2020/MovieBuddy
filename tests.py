from app import app

with app.test_client() as client:

    # testing main application routes
    response = client.get('/')
    assert response.status_code == 200

    response2 = client.post('/')
    assert response2.status_code == 400
