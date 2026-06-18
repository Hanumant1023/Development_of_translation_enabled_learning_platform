from deep_translator import GoogleTranslator
import asyncio

SEP = "\n|||\n"
PLACEHOLDER = " [|||] "
MAX_CHARS = 4500

def _translate_sync(text: str, target_lang: str) -> str:
    """Translate text, chunking if it exceeds Google's limit."""
    safe = text.replace(SEP, PLACEHOLDER)
    if len(safe) <= MAX_CHARS:
        result = GoogleTranslator(source="en", target=target_lang).translate(safe)
        return (result or text).replace(PLACEHOLDER, SEP)

    # Split into chunks at PLACEHOLDER boundaries
    parts = safe.split(PLACEHOLDER)
    chunks, current = [], ""
    for part in parts:
        candidate = current + (PLACEHOLDER if current else "") + part
        if len(candidate) > MAX_CHARS and current:
            chunks.append(current)
            current = part
        else:
            current = candidate
    if current:
        chunks.append(current)

    translated_chunks = [
        GoogleTranslator(source="en", target=target_lang).translate(c) or c
        for c in chunks
    ]
    return PLACEHOLDER.join(translated_chunks).replace(PLACEHOLDER, SEP)

async def translate_text(text: str, target_lang: str) -> str:
    if not text or not text.strip():
        return text
    try:
        return await asyncio.to_thread(_translate_sync, text, target_lang)
    except Exception:
        return text
