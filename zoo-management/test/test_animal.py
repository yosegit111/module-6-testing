# test/test_animal.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_animals(client):
    """Test the /animals GET route."""
    response = client.get('/animals')
    assert response.status_code == 200

    assert b"Add New Animal" in response.data
    assert b"Update</button>" in response.data
    assert b"Delete</button>" in response.data


def test_add_animal(client):
    """Test the /animals POST route."""
    new_animal = {
        'name': 'Lion',
        'species': 'Panthera leo',
        'age': 5,
        'gender': 'Male',
        'area_code': 'Mammals'
    }
    response = client.post('/animals', json=new_animal)
    assert response.status_code == 201
    assert response.json['name'] == 'Lion'
