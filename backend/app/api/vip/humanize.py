from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.vip.humanize import humanize_content

router = APIRouter()

class HumanizeRequest(BaseModel):
    text: str
    style: str = "conversational"  # conversational, professional, casual, creative
    
class HumanizeResponse(BaseModel):
    humanized_text: str
    changes_made: int

@router.post("/humanize", response_model=HumanizeResponse)
async def content_humanization(request: HumanizeRequest):
    """
    Make machine-generated content sound more human.
    """
    try:
        result = await humanize_content(
            text=request.text,
            style=request.style
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 