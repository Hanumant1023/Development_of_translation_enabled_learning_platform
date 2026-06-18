from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from bson import ObjectId
from bson.errors import InvalidId
from config.db import db

router = APIRouter()

class ArticleBody(BaseModel):
    title: str
    content: str
    category: str
    author: Optional[str] = "Admin"

def serialize(article):
    article["id"] = str(article["_id"])
    del article["_id"]
    return article

@router.get("/")
async def get_all():
    articles = list(db.articles.find().sort("createdAt", -1))
    return [serialize(a) for a in articles]

@router.get("/{article_id}")
async def get_one(article_id: str):
    try:
        oid = ObjectId(article_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid article ID")
    article = db.articles.find_one({"_id": oid})
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return serialize(article)

@router.post("/", status_code=201)
async def create(body: ArticleBody):
    result = db.articles.insert_one({**body.dict(), "createdAt": datetime.now(timezone.utc)})
    article = db.articles.find_one({"_id": result.inserted_id})
    return serialize(article)
