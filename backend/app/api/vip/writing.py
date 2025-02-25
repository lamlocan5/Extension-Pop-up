from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.vip.writing import enhance_writing

router = APIRouter()

class WritingRequest(BaseModel):
    text: str
    tone: str = "professional"  # professional, casual, academic, creative
    target_audience: str = "general"

class Suggestion(BaseModel):
    original: str
    improved: str
    explanation: str

class WritingResponse(BaseModel):
    improved_text: str
    suggestions: List[Suggestion] = []
    readability_score: float

@router.post("/writing", response_model=WritingResponse)
async def writing_enhancement(request: WritingRequest):
    """
    Enhance writing with suggestions for improvement.
    """
    try:
        result = await enhance_writing(
            text=request.text,
            tone=request.tone,
            target_audience=request.target_audience
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 