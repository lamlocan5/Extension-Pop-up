from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import translation, tts, grammar, flashcards, images, summary
from app.api.vip import accent, writing, detection, humanize
from app.core.config import settings
from app.core.database import create_db_and_tables

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.API_VERSION,
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(translation.router, prefix="/api/v1", tags=["translation"])
app.include_router(tts.router, prefix="/api/v1", tags=["text-to-speech"])
app.include_router(grammar.router, prefix="/api/v1", tags=["grammar"])
app.include_router(flashcards.router, prefix="/api/v1", tags=["flashcards"])
app.include_router(images.router, prefix="/api/v1", tags=["images"])
app.include_router(summary.router, prefix="/api/v1", tags=["summarization"])

# Include VIP routers
app.include_router(accent.router, prefix="/api/v1/vip", tags=["accent"])
app.include_router(writing.router, prefix="/api/v1/vip", tags=["writing"])
app.include_router(detection.router, prefix="/api/v1/vip", tags=["detection"])
app.include_router(humanize.router, prefix="/api/v1/vip", tags=["humanize"])

@app.on_event("startup")
async def on_startup():
    # Create database tables on startup
    create_db_and_tables()

@app.get("/api/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}
