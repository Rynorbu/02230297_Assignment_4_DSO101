import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['message'] == 'Hello, World!'

def test_add(client):
    """Test the add endpoint"""
    response = client.get('/api/add/10/5')
    assert response.status_code == 200
    assert response.json['result'] == 15
    assert response.json['operation'] == 'addition'

def test_subtract(client):
    """Test the subtract endpoint"""
    response = client.get('/api/subtract/10/3')
    assert response.status_code == 200
    assert response.json['result'] == 7
    assert response.json['operation'] == 'subtraction'

def test_health(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_add_zero(client):
    """Test add endpoint with zero"""
    response = client.get('/api/add/0/5')
    assert response.status_code == 200
    assert response.json['result'] == 5

def test_subtract_same_numbers(client):
    """Test subtract endpoint with same numbers"""
    response = client.get('/api/subtract/10/10')
    assert response.status_code == 200
    assert response.json['result'] == 0
