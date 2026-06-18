from fastapi import APIRouter
from pydantic import BaseModel
from config.translation import translate_text

router = APIRouter()

class TranslateBody(BaseModel):
    text: str
    targetLang: str

@router.post("/")
async def translate(body: TranslateBody):
    try:
        translated = await translate_text(body.text, body.targetLang)
        return {"translated": translated}
    except Exception:
        return {"translated": body.text}
