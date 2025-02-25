from fastapi import APIRouter

from app.api.routes import translation, tts, grammar, flashcards, images, summary

router = APIRouter()

router.include_router(translation.router, tags=["translation"])
router.include_router(tts.router, tags=["text-to-speech"])
router.include_router(grammar.router, tags=["grammar"])
router.include_router(flashcards.router, tags=["flashcards"])
router.include_router(images.router, tags=["images"])
router.include_router(summary.router, tags=["summarization"])
