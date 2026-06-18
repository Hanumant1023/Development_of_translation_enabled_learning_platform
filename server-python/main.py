from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.articles import router as articles_router
from routes.units import router as units_router
from routes.translate import router as translate_router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(redirect_slashes=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router,      prefix="/api/auth")
app.include_router(articles_router,  prefix="/api/articles")
app.include_router(units_router,     prefix="/api/units")
app.include_router(translate_router, prefix="/api/translate")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 5000)), reload=True)
