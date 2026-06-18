from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timezone
from bson import ObjectId
from bson.errors import InvalidId
from config.db import db

router = APIRouter()

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: int

class Section(BaseModel):
    heading: Optional[str] = ""
    body_html: str
    summary: Optional[str] = ""

class UnitBody(BaseModel):
    title: str
    unit_number: int
    content: str
    category: str
    author: Optional[str] = "Admin"
    quiz: List[QuizQuestion] = []
    sections: List[Section] = []

def serialize(unit):
    unit["id"] = str(unit["_id"])
    del unit["_id"]
    unit.setdefault("sections", [])
    unit.setdefault("quiz", [])
    return unit

@router.get("/")
async def get_all():
    units = list(db.units.find().sort([("category", 1), ("unit_number", 1)]))
    return [serialize(u) for u in units]

@router.post("/track")
async def track(body: dict):
    from bson import ObjectId
    from middleware.auth import verify_token
    token = body.get("token", "")
    unit_id = body.get("unit_id", "")
    try:
        payload = verify_token(token)
        user_oid = ObjectId(payload["id"])
        unit = db.units.find_one({"_id": ObjectId(unit_id)})
        if unit:
            db.users.update_one(
                {"_id": user_oid},
                {"$set": {"lastStudied": {
                    "unit_id": unit_id,
                    "title": unit.get("title", ""),
                    "category": unit.get("category", ""),
                    "at": datetime.now(timezone.utc)
                }}}
            )
    except Exception:
        pass
    return {"ok": True}

@router.get("/{unit_id}")
async def get_one(unit_id: str):
    try:
        oid = ObjectId(unit_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid unit ID")
    unit = db.units.find_one({"_id": oid})
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return serialize(unit)

async def create(body: UnitBody):
    result = db.units.insert_one({**body.dict(), "createdAt": datetime.now(timezone.utc)})
    unit = db.units.find_one({"_id": result.inserted_id})
    return serialize(unit)
