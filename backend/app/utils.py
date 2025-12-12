from jose import jwt, JWTError
from passlib.context import CryptContext
from app.models import User

# JWT Secret Key
SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Context
pwd_context = CryptContext(schemes=["bcrypt"])