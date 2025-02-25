from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.summary import summarize_text

router = APIRouter()

class SummaryRequest(BaseModel):
    text: str
    max_length: int = 200

class SummaryResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int

@router.post("/summary", response_model=SummaryResponse)
async def get_summary(request: SummaryRequest):
    """
    Generate a summary of the text.
    """
    try:
        summary = await summarize_text(
            text=request.text,
            max_length=request.max_length
        )
        
        return {
            "summary": summary,
            "original_length": len(request.text),
            "summary_length": len(summary)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 