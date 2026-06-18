from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, EmailStr
import bcrypt
import jwt
import os
from datetime import datetime, timezone, timedelta
from config.db import db
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class RegisterBody(BaseModel):
    name: str
    email: str
    password: str
    preferredLanguage: str = "hi"

class LoginBody(BaseModel):
    email: str
    password: str

def sign_token(user_id: str):
    payload = {"id": user_id, "exp": datetime.now(timezone.utc) + timedelta(days=7)}
    return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")

@router.post("/register", status_code=201)
async def register(body: RegisterBody):
    email = body.email.strip().lower()
    if db.users.find_one({"email": {"$eq": email}}):
        raise HTTPException(status_code=400, detail="Email already exists")
    hashed = bcrypt.hashpw(body.password.encode(), bcrypt.gensalt())
    result = db.users.insert_one({
        "name": body.name.strip(),
        "email": email,
        "password": hashed.decode(),
        "preferredLanguage": body.preferredLanguage,
        "createdAt": datetime.now(timezone.utc)
    })
    user_id = str(result.inserted_id)
    return {
        "token": sign_token(user_id),
        "user": {"id": user_id, "name": body.name, "email": email, "preferredLanguage": body.preferredLanguage}
    }

@router.get("/me")
async def me(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No token")
    try:
        payload = jwt.decode(authorization.split(" ")[1], os.getenv("JWT_SECRET"), algorithms=["HS256"])
        from bson import ObjectId
        user = db.users.find_one({"_id": ObjectId(payload["id"])})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        ls = user.get("lastStudied")
        last_studied = None
        if ls:
            last_studied = {
                "unit_id": ls.get("unit_id", ""),
                "title": ls.get("title", ""),
                "category": ls.get("category", ""),
                "at": ls["at"].strftime("%d %b %Y, %I:%M %p") if ls.get("at") else ""
            }
        return {"lastStudied": last_studied}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/login")
async def login(body: LoginBody):
    email = body.email.strip().lower()
    user = db.users.find_one({"email": {"$eq": email}})
    if not user or not bcrypt.checkpw(body.password.encode(), user["password"].encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    user_id = str(user["_id"])
    return {
        "token": sign_token(user_id),
        "user": {"id": user_id, "name": user["name"], "email": email, "preferredLanguage": user.get("preferredLanguage", "hi")}
    }
