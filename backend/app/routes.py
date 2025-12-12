from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.utils import validate_token
from app.models import User, Data

router = APIRouter(
    prefix='/api',
    tags=['users'],
)

# Health Check
@router.get('/health')
def health_check():
    return { 'status': 'ok', 'timestamp': 'now' }

# User Routes
@router.get('/users')
def get_users(token: str = Depends(validate_token)):    return { 'users': User.query.all(), 'total': len(User.query.all()) }

@router.post('/users')
def create_user(name: str, email: str, token: str = Depends(validate_token)):    user = User(username=name, email=email)
    db.session.add(user)
    db.session.commit()
    return { 'id': user.id, 'name': user.username, 'email': user.email }

@router.get('/users/{user_id}')
def get_user(user_id: int, token: str = Depends(validate_token)):    return { 'id': User.query.get(user_id).id, 'name': User.query.get(user_id).username, 'email': User.query.get(user_id).email }

@router.put('/users/{user_id}')
def update_user(user_id: int, name: str, email: str, token: str = Depends(validate_token)):    user = User.query.get(user_id)
    user.username = name
    user.email = email
    db.session.commit()
    return { 'id': user.id, 'name': user.username, 'email': user.email }

@router.delete('/users/{user_id}')
def delete_user(user_id: int, token: str = Depends(validate_token)):    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return { 'message': 'User deleted successfully' }

# Data Routes
@router.get('/data')
def get_data(token: str = Depends(validate_token)):    return { 'data': Data.query.all(), 'total': len(Data.query.all()) }

@router.post('/data')
def create_data(name: str, description: str, token: str = Depends(validate_token)):    data = Data(name=name, description=description, user_id=User.query.first().id)
    db.session.add(data)
    db.session.commit()
    return { 'id': data.id, 'name': data.name, 'description': data.description }

@router.put('/data/{data_id}')
def update_data(data_id: int, name: str, description: str, token: str = Depends(validate_token)):    data = Data.query.get(data_id)
    data.name = name
    data.description = description
    db.session.commit()
    return { 'message': 'Data updated successfully' }

@router.delete('/data/{data_id}')
def delete_data(data_id: int, token: str = Depends(validate_token)):    data = Data.query.get(data_id)
    db.session.delete(data)
    db.session.commit()
    return { 'message': 'Data deleted successfully' }
