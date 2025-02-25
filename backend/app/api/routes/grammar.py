from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.grammar import check_grammar

router = APIRouter()

class GrammarRequest(BaseModel):
    text: str
    language: str = "en-US"

class GrammarError(BaseModel):
    start: int
    end: int
    message: str
    suggestions: List[str] = []

class GrammarResponse(BaseModel):
    text: str
    errors: List[GrammarError] = []
    improved_text: str = None

@router.post("/grammar", response_model=GrammarResponse)
async def grammar_check(request: GrammarRequest):
    """
    Check grammar and suggest improvements.
    """
    try:
        result = await check_grammar(
            text=request.text,
            language=request.language
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 