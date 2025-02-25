from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.tts import text_to_speech

router = APIRouter()

class TTSRequest(BaseModel):
    text: str
    language_code: str = "en-US"
    voice_name: str = "en-US-Standard-A"

class TTSResponse(BaseModel):
    audio_content: str  # Base64 encoded audio content

@router.post("/tts", response_model=TTSResponse)
async def generate_speech(request: TTSRequest):
    """
    Convert text to speech.
    """
    try:
        result = await text_to_speech(
            text=request.text,
            language_code=request.language_code,
            voice_name=request.voice_name
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 