from datetime import timedelta, datetime
import jwt
from passlib.context import CryptContext
import uuid
import logging
from ..config import Config

passwd_context = CryptContext(
    schemes=['bcrypt']
)

def generate_password_hash(password: str) -> str:
    hash_password = passwd_context.hash(password)
    return hash_password

def verify_password(password: str, hashed_password: str) -> bool:
    return passwd_context.verify(password, hashed_password)

def create_access_token(
        user_data: dict,
        expiry:timedelta =None,
        refresh: bool= False) -> str:
    payload = {
        'exp': datetime.now() + (expiry if expiry is not None else timedelta(minutes=60)),
        'user': user_data,
        'jti': str(uuid.uuid4()),
        'refresh': refresh,
    }
    token = jwt.encode(
        payload=payload,
        algorithm='HS256',
        key=Config.JWT_SECRET,
    )
    return token

def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            algorithms=Config.JWT_ALGORITHM,
            key=Config.JWT_SECRET,
        )

        return token_data
    except jwt.PyJWTError as e:
        logging.exception(e)
        return {}

    except Exception as e:
        logging.exception(e)
        return {}
