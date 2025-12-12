import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Health Check
def test_health_check():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json() == { 'status': 'ok', 'timestamp': 'now' }

# User Routes
def test_get_users():
    response = client.get('/api/users')
    assert response.status_code == 401

def test_create_user():
    response = client.post('/api/users', json={ 'name': 'test_user', 'email': 'test@example.com' })
    assert response.status_code == 401

def test_get_user():
    response = client.get('/api/users/1')
    assert response.status_code == 401

def test_update_user():
    response = client.put('/api/users/1', json={ 'name': 'updated_user', 'email': 'updated@example.com' })
    assert response.status_code == 401

def test_delete_user():
    response = client.delete('/api/users/1')
    assert response.status_code == 401

# Data Routes
def test_get_data():
    response = client.get('/api/data')
    assert response.status_code == 401

def test_create_data():
    response = client.post('/api/data', json={ 'name': 'test_data', 'description': 'test description' })
    assert response.status_code == 401

def test_update_data():
    response = client.put('/api/data/1', json={ 'name': 'updated_data', 'description': 'updated description' })
    assert response.status_code == 401

def test_delete_data():
    response = client.delete('/api/data/1')
    assert response.status_code == 401
