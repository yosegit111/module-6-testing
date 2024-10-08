def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to RevoU Zoo Management Service" in response.data

def test_animal_page(client):
    response = client.get('/animals')
    assert response.status_code == 200

def test_employee_page(client):
    response = client.get('/employees')
    assert response.status_code == 200
