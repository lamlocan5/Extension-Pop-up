from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.translation import translate_text

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class TranslationResponse(BaseModel):
    translated_text: str
    source_language: str
    phonetics: str = None
    definitions: list[str] = None

@router.post("/translation", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    """
    Translate text to the target language.
    """
    try:
        result = await translate_text(
            text=request.text,
            target_language=request.target_language
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
