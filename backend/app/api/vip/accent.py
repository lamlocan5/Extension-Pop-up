from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
from app.services.vip.accent import check_accent

router = APIRouter()

class AccentFeedback(BaseModel):
    text: str
    score: float
    issues: List[str] = []
    suggestions: List[str] = []

class AccentResponse(BaseModel):
    overall_score: float
    feedback: AccentFeedback

@router.post("/accent", response_model=AccentResponse)
async def accent_check(reference_text: str, audio_file: UploadFile = File(...)):
    """
    Check accent pronunciation against reference text.
    """
    try:
        audio_content = await audio_file.read()
        result = await check_accent(
            audio_content=audio_content,
            reference_text=reference_text
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 