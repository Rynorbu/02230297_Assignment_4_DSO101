from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Hello, World!',
        'status': 'success',
        'app': 'DSO101 Assignment 4 - CI/CD Pipeline'
    })

@app.route('/api/add/<int:a>/<int:b>')
def add(a, b):
    """Add two numbers endpoint"""
    return jsonify({
        'a': a,
        'b': b,
        'result': a + b,
        'operation': 'addition'
    })

@app.route('/api/subtract/<int:a>/<int:b>')
def subtract(a, b):
    """Subtract two numbers endpoint"""
    return jsonify({
        'a': a,
        'b': b,
        'result': a - b,
        'operation': 'subtraction'
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
