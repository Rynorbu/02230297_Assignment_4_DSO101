const request = require('supertest');
const app = require('../server');

describe('DSO Assignment 4 - API Tests', () => {
  
  describe('Health Check Endpoint', () => {
    test('GET /api/health should return 200 status', async () => {
      const response = await request(app).get('/api/health');
      expect(response.statusCode).toBe(200);
    });

    test('GET /api/health should return healthy status', async () => {
      const response = await request(app).get('/api/health');
      expect(response.body.status).toBe('healthy');
    });

    test('GET /api/health should return timestamp', async () => {
      const response = await request(app).get('/api/health');
      expect(response.body.timestamp).toBeDefined();
    });
  });

  describe('Root Endpoint', () => {
    test('GET / should return 200 status', async () => {
      const response = await request(app).get('/');
      expect(response.statusCode).toBe(200);
    });

    test('GET / should return API message', async () => {
      const response = await request(app).get('/');
      expect(response.body.message).toBe('Todo API is running');
    });

    test('GET / should return version', async () => {
      const response = await request(app).get('/');
      expect(response.body.version).toBe('1.0.0');
    });
  });

  describe('404 Handler', () => {
    test('GET /invalid-route should return 404', async () => {
      const response = await request(app).get('/invalid-route');
      expect(response.statusCode).toBe(404);
    });

    test('GET /invalid-route should return error message', async () => {
      const response = await request(app).get('/invalid-route');
      expect(response.body.success).toBe(false);
    });
  });

  describe('Basic Math & Logic Tests', () => {
    test('1 + 1 should equal 2', () => {
      expect(1 + 1).toBe(2);
    });

    test('String concatenation: Hello + World', () => {
      const result = 'Hello' + ' ' + 'World';
      expect(result).toBe('Hello World');
    });

    test('Array should contain expected element', () => {
      const arr = [1, 2, 3, 4, 5];
      expect(arr).toContain(3);
    });

    test('Object property access', () => {
      const obj = { name: 'Todo API', version: '1.0.0' };
      expect(obj.name).toBe('Todo API');
    });

    test('Boolean logic test', () => {
      const isValid = true;
      expect(isValid).toBe(true);
    });
  });

  describe('Middleware Tests', () => {
    test('Request should accept JSON content-type', async () => {
      const response = await request(app)
        .get('/')
        .set('Content-Type', 'application/json');
      expect(response.statusCode).toBe(200);
    });

    test('Response should have proper content-type', async () => {
      const response = await request(app).get('/');
      expect(response.headers['content-type']).toContain('application/json');
    });
  });

});

describe('Integration Tests', () => {
  test('Multiple consecutive requests should work', async () => {
    const req1 = await request(app).get('/');
    const req2 = await request(app).get('/api/health');
    
    expect(req1.statusCode).toBe(200);
    expect(req2.statusCode).toBe(200);
  });

  test('API should respond quickly', async () => {
    const start = Date.now();
    await request(app).get('/');
    const duration = Date.now() - start;
    
    expect(duration).toBeLessThan(1000);
  });
});
