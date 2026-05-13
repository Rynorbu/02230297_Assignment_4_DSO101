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

# ============================================
# ADVANCED ARITHMETIC TESTS
# ============================================

def test_multiply(client):
    """Test the multiply endpoint"""
    response = client.get('/api/multiply/6/7')
    assert response.status_code == 200
    assert response.json['result'] == 42
    assert response.json['operation'] == 'multiplication'

def test_divide(client):
    """Test the divide endpoint"""
    response = client.get('/api/divide/20/4')
    assert response.status_code == 200
    assert response.json['result'] == 5.0
    assert response.json['operation'] == 'division'

def test_divide_by_zero(client):
    """Test divide by zero error handling"""
    response = client.get('/api/divide/10/0')
    assert response.status_code == 400
    assert response.json['error'] == 'Cannot divide by zero'

def test_power(client):
    """Test the power endpoint"""
    response = client.get('/api/power/2/3')
    assert response.status_code == 200
    assert response.json['result'] == 8
    assert response.json['operation'] == 'exponentiation'

def test_sqrt(client):
    """Test the square root endpoint"""
    response = client.get('/api/sqrt/16')
    assert response.status_code == 200
    assert response.json['result'] == 4.0
    assert response.json['operation'] == 'square root'

def test_sqrt_negative(client):
    """Test square root with negative number"""
    response = client.get('/api/sqrt/-9')
    assert response.status_code == 400
    assert 'error' in response.json

def test_factorial(client):
    """Test the factorial endpoint"""
    response = client.get('/api/factorial/5')
    assert response.status_code == 200
    assert response.json['result'] == 120

# ============================================
# CONVERTER TESTS
# ============================================

def test_celsius_to_fahrenheit(client):
    """Test temperature conversion"""
    response = client.get('/api/temperature/celsius-to-fahrenheit/0')
    assert response.status_code == 200
    assert response.json['output']['fahrenheit'] == 32.0

def test_fahrenheit_to_celsius(client):
    """Test Fahrenheit to Celsius conversion"""
    response = client.get('/api/temperature/fahrenheit-to-celsius/32')
    assert response.status_code == 200
    assert response.json['output']['celsius'] == 0.0

# ============================================
# CALCULATOR TESTS
# ============================================

def test_bmi(client):
    """Test BMI calculator"""
    response = client.get('/api/bmi/70/1.75')
    assert response.status_code == 200
    assert 'bmi' in response.json
    assert 'category' in response.json
    assert response.json['weight_kg'] == 70

def test_bmi_invalid(client):
    """Test BMI with invalid input"""
    response = client.get('/api/bmi/-70/1.75')
    assert response.status_code == 400
    assert 'error' in response.json

def test_grade_excellent(client):
    """Test grade calculator for excellent score"""
    response = client.get('/api/grade/95')
    assert response.status_code == 200
    assert response.json['grade'] == 'A'
    assert response.json['description'] == 'Excellent'

def test_grade_fail(client):
    """Test grade calculator for failing score"""
    response = client.get('/api/grade/45')
    assert response.status_code == 200
    assert response.json['grade'] == 'F'
    assert response.json['description'] == 'Fail'

def test_grade_invalid(client):
    """Test grade with invalid score"""
    response = client.get('/api/grade/150')
    assert response.status_code == 400

# ============================================
# STRING OPERATIONS TESTS
# ============================================

def test_reverse_string(client):
    """Test string reversal"""
    response = client.get('/api/string/reverse/hello')
    assert response.status_code == 200
    assert response.json['reversed'] == 'olleh'

def test_uppercase(client):
    """Test uppercase conversion"""
    response = client.get('/api/string/uppercase/hello')
    assert response.status_code == 200
    assert response.json['uppercase'] == 'HELLO'

def test_lowercase(client):
    """Test lowercase conversion"""
    response = client.get('/api/string/lowercase/HELLO')
    assert response.status_code == 200
    assert response.json['lowercase'] == 'hello'

def test_string_length(client):
    """Test string length calculation"""
    response = client.get('/api/string/length/python')
    assert response.status_code == 200
    assert response.json['length'] == 6

# ============================================
# STATISTICS TESTS
# ============================================

def test_average(client):
    """Test average calculation"""
    response = client.post('/api/statistics/average',
                          json={'numbers': [1, 2, 3, 4, 5]})
    assert response.status_code == 200
    assert response.json['average'] == 3.0
    assert response.json['sum'] == 15

def test_statistics_sum(client):
    """Test sum calculation"""
    response = client.post('/api/statistics/sum',
                          json={'numbers': [10, 20, 30]})
    assert response.status_code == 200
    assert response.json['sum'] == 60

# ============================================
# INFO & UTILITY TESTS
# ============================================

def test_info_endpoint(client):
    """Test info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    assert response.json['version'] == '2.0'
    assert 'features' in response.json

def test_404_error(client):
    """Test 404 error handling"""
    response = client.get('/api/nonexistent')
    assert response.status_code == 404
    assert 'error' in response.json
