from fastapi import Header, HTTPException
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

def verify_token(token: str):
    return jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])

def auth_middleware(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No token provided")
    try:
        return verify_token(authorization.split(" ")[1])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
