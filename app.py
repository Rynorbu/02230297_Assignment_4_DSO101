from flask import Flask, jsonify, request
import math
from datetime import datetime

app = Flask(__name__)

# ============================================
# HOME & UTILITY ENDPOINTS
# ============================================

@app.route('/')
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        'message': 'Hello, World!',
        'status': 'success',
        'app': 'DSO101 Assignment 4 - CI/CD Pipeline',
        'version': '2.0',
        'timestamp': datetime.now().isoformat(),
        'available_endpoints': {
            'math': [
                '/api/add/<a>/<b> - Add two numbers',
                '/api/subtract/<a>/<b> - Subtract two numbers',
                '/api/multiply/<a>/<b> - Multiply two numbers',
                '/api/divide/<a>/<b> - Divide two numbers',
                '/api/power/<base>/<exponent> - Calculate power',
                '/api/sqrt/<number> - Calculate square root'
            ],
            'tools': [
                '/api/temperature/celsius-to-fahrenheit/<celsius> - Convert temperature',
                '/api/bmi/<weight>/<height> - Calculate BMI (weight in kg, height in m)',
                '/api/grade/<score> - Calculate letter grade',
                '/api/factorial/<number> - Calculate factorial',
                '/api/statistics/average - POST with {"numbers": [1,2,3]} to calculate average'
            ],
            'utility': [
                '/health - Health check',
                '/api/info - Get application info'
            ]
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/info')
def info():
    """Application information"""
    return jsonify({
        'app_name': 'Advanced Calculator API',
        'version': '2.0',
        'course': 'DSO101 - CI/CD Pipeline',
        'features': [
            'Basic arithmetic operations',
            'Temperature conversion',
            'BMI calculator',
            'Grade calculator',
            'Advanced mathematics'
        ],
        'deployment': 'Render Cloud Platform',
        'ci_cd': 'GitHub Actions'
    })

# ============================================
# BASIC ARITHMETIC ENDPOINTS
# ============================================

@app.route('/api/add/<int:a>/<int:b>')
def add(a, b):
    """Add two numbers endpoint"""
    return jsonify({
        'a': a,
        'b': b,
        'result': a + b,
        'operation': 'addition',
        'formula': f'{a} + {b}'
    })

@app.route('/api/subtract/<int:a>/<int:b>')
def subtract(a, b):
    """Subtract two numbers endpoint"""
    return jsonify({
        'a': a,
        'b': b,
        'result': a - b,
        'operation': 'subtraction',
        'formula': f'{a} - {b}'
    })

# ============================================
# ADVANCED ARITHMETIC ENDPOINTS
# ============================================

@app.route('/api/multiply/<int:a>/<int:b>')
def multiply(a, b):
    """Multiply two numbers"""
    result = a * b
    return jsonify({
        'a': a,
        'b': b,
        'result': result,
        'operation': 'multiplication',
        'formula': f'{a} × {b} = {result}'
    })

@app.route('/api/divide/<int:a>/<int:b>')
def divide(a, b):
    """Divide two numbers with error handling"""
    if b == 0:
        return jsonify({
            'error': 'Cannot divide by zero',
            'status': 'error',
            'code': 400
        }), 400
    
    result = a / b
    return jsonify({
        'a': a,
        'b': b,
        'result': round(result, 2),
        'operation': 'division',
        'formula': f'{a} ÷ {b} = {round(result, 2)}'
    })

@app.route('/api/power/<int:base>/<int:exponent>')
def power(base, exponent):
    """Calculate power (base^exponent)"""
    result = base ** exponent
    return jsonify({
        'base': base,
        'exponent': exponent,
        'result': result,
        'operation': 'exponentiation',
        'formula': f'{base}^{exponent} = {result}'
    })

@app.route('/api/sqrt/<number>')
def sqrt(number):
    """Calculate square root"""
    try:
        num = float(number)
    except ValueError:
        return jsonify({
            'error': 'Number must be a valid number',
            'status': 'error',
            'code': 400
        }), 400
    
    if num < 0:
        return jsonify({
            'error': 'Cannot calculate square root of negative number',
            'status': 'error',
            'code': 400
        }), 400
    
    result = math.sqrt(num)
    return jsonify({
        'number': num,
        'result': round(result, 4),
        'operation': 'square root',
        'formula': f'√{num} = {round(result, 4)}'
    })

@app.route('/api/factorial/<int:number>')
def factorial(number):
    """Calculate factorial"""
    if number < 0:
        return jsonify({
            'error': 'Factorial not defined for negative numbers',
            'status': 'error',
            'code': 400
        }), 400
    
    result = math.factorial(number)
    return jsonify({
        'number': number,
        'result': result,
        'operation': 'factorial',
        'formula': f'{number}! = {result}'
    })

# ============================================
# CONVERTER ENDPOINTS
# ============================================

@app.route('/api/temperature/celsius-to-fahrenheit/<celsius>')
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    try:
        celsius_val = float(celsius)
    except ValueError:
        return jsonify({
            'error': 'Temperature must be a valid number',
            'status': 'error',
            'code': 400
        }), 400
    
    fahrenheit = (celsius_val * 9/5) + 32
    kelvin = celsius_val + 273.15
    
    return jsonify({
        'input': {
            'value': celsius_val,
            'unit': 'Celsius (°C)'
        },
        'output': {
            'fahrenheit': round(fahrenheit, 2),
            'kelvin': round(kelvin, 2)
        },
        'conversions': {
            'celsius_to_fahrenheit': f'{celsius_val}°C = {round(fahrenheit, 2)}°F',
            'celsius_to_kelvin': f'{celsius_val}°C = {round(kelvin, 2)}K'
        }
    })

@app.route('/api/temperature/fahrenheit-to-celsius/<fahrenheit>')
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    try:
        fahrenheit_val = float(fahrenheit)
    except ValueError:
        return jsonify({
            'error': 'Temperature must be a valid number',
            'status': 'error',
            'code': 400
        }), 400
    
    celsius = (fahrenheit_val - 32) * 5/9
    kelvin = celsius + 273.15
    
    return jsonify({
        'input': {
            'value': fahrenheit_val,
            'unit': 'Fahrenheit (°F)'
        },
        'output': {
            'celsius': round(celsius, 2),
            'kelvin': round(kelvin, 2)
        },
        'conversions': {
            'fahrenheit_to_celsius': f'{fahrenheit_val}°F = {round(celsius, 2)}°C',
            'fahrenheit_to_kelvin': f'{fahrenheit_val}°F = {round(kelvin, 2)}K'
        }
    })

# ============================================
# CALCULATOR ENDPOINTS
# ============================================

@app.route('/api/bmi/<weight>/<height>')
def bmi(weight, height):
    """Calculate BMI (weight in kg, height in meters)"""
    try:
        weight_val = float(weight)
        height_val = float(height)
    except ValueError:
        return jsonify({
            'error': 'Weight and height must be valid numbers',
            'status': 'error',
            'code': 400
        }), 400
    
    if weight_val <= 0 or height_val <= 0:
        return jsonify({
            'error': 'Weight and height must be positive values',
            'status': 'error',
            'code': 400
        }), 400
    
    bmi_value = weight_val / (height_val ** 2)
    
    # Determine BMI category
    if bmi_value < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi_value < 25:
        category = 'Normal weight'
    elif 25 <= bmi_value < 30:
        category = 'Overweight'
    else:
        category = 'Obese'
    
    return jsonify({
        'weight_kg': weight_val,
        'height_m': height_val,
        'bmi': round(bmi_value, 2),
        'category': category,
        'formula': f'BMI = {weight_val} / ({height_val}²) = {round(bmi_value, 2)}',
        'health_info': {
            'underweight': 'BMI < 18.5',
            'normal': '18.5 ≤ BMI < 25',
            'overweight': '25 ≤ BMI < 30',
            'obese': 'BMI ≥ 30'
        }
    })

@app.route('/api/grade/<int:score>')
def grade_calculator(score):
    """Calculate letter grade based on score (0-100)"""
    if score < 0 or score > 100:
        return jsonify({
            'error': 'Score must be between 0 and 100',
            'status': 'error',
            'code': 400
        }), 400
    
    # Grading scale
    if score >= 90:
        grade = 'A'
        description = 'Excellent'
    elif score >= 80:
        grade = 'B'
        description = 'Good'
    elif score >= 70:
        grade = 'C'
        description = 'Satisfactory'
    elif score >= 60:
        grade = 'D'
        description = 'Acceptable'
    else:
        grade = 'F'
        description = 'Fail'
    
    return jsonify({
        'score': score,
        'grade': grade,
        'description': description,
        'grade_scale': {
            'A': '90-100 (Excellent)',
            'B': '80-89 (Good)',
            'C': '70-79 (Satisfactory)',
            'D': '60-69 (Acceptable)',
            'F': '0-59 (Fail)'
        }
    })

# ============================================
# STATISTICS ENDPOINTS
# ============================================

@app.route('/api/statistics/average', methods=['POST'])
def calculate_average():
    """Calculate average of numbers - POST with JSON: {"numbers": [1, 2, 3]}"""
    try:
        data = request.get_json()
        
        if not data or 'numbers' not in data:
            return jsonify({
                'error': 'Invalid request. Send JSON with "numbers" array',
                'example': '{"numbers": [1, 2, 3, 4, 5]}',
                'status': 'error',
                'code': 400
            }), 400
        
        numbers = data['numbers']
        
        if not numbers:
            return jsonify({
                'error': 'Numbers array cannot be empty',
                'status': 'error',
                'code': 400
            }), 400
        
        average = sum(numbers) / len(numbers)
        
        return jsonify({
            'numbers': numbers,
            'count': len(numbers),
            'sum': sum(numbers),
            'average': round(average, 2),
            'min': min(numbers),
            'max': max(numbers)
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error',
            'code': 400
        }), 400

@app.route('/api/statistics/sum', methods=['POST'])
def calculate_sum():
    """Calculate sum of numbers - POST with JSON: {"numbers": [1, 2, 3]}"""
    try:
        data = request.get_json()
        
        if not data or 'numbers' not in data:
            return jsonify({
                'error': 'Invalid request. Send JSON with "numbers" array',
                'status': 'error',
                'code': 400
            }), 400
        
        numbers = data['numbers']
        total = sum(numbers)
        
        return jsonify({
            'numbers': numbers,
            'count': len(numbers),
            'sum': total,
            'average': round(total / len(numbers), 2) if numbers else 0
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error',
            'code': 400
        }), 400

# ============================================
# STRING OPERATIONS ENDPOINTS
# ============================================

@app.route('/api/string/reverse/<string:text>')
def reverse_string(text):
    """Reverse a string"""
    reversed_text = text[::-1]
    return jsonify({
        'original': text,
        'reversed': reversed_text,
        'operation': 'string reversal'
    })

@app.route('/api/string/uppercase/<string:text>')
def uppercase_string(text):
    """Convert string to uppercase"""
    return jsonify({
        'original': text,
        'uppercase': text.upper(),
        'operation': 'uppercase conversion'
    })

@app.route('/api/string/lowercase/<string:text>')
def lowercase_string(text):
    """Convert string to lowercase"""
    return jsonify({
        'original': text,
        'lowercase': text.lower(),
        'operation': 'lowercase conversion'
    })

@app.route('/api/string/length/<string:text>')
def string_length(text):
    """Calculate string length"""
    return jsonify({
        'text': text,
        'length': len(text),
        'characters': list(text),
        'vowels': sum(1 for char in text.lower() if char in 'aeiou'),
        'consonants': sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiou')
    })

# ============================================
# ERROR HANDLING
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'status': 'error',
        'code': 404,
        'hint': 'Visit / for available endpoints'
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'status': 'error',
        'code': 500
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
