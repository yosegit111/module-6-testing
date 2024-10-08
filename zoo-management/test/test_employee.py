# test/test_employee.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_employees(client):
    """Test the /employees GET route."""
    response = client.get('/employees')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_employee(client):
    """Test the /employees POST route."""
    new_employee = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'phone_number': '123456789',
        'role': 'Caretaker',
        'schedule': 'Monday Morning'
    }
    response = client.post('/employees', json=new_employee)
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'
