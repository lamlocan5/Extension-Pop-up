from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.flashcards import create_flashcard, get_flashcards, get_flashcard_by_id, delete_flashcard

router = APIRouter()

class FlashcardBase(BaseModel):
    front: str
    back: str
    context: Optional[str] = None
    language: str = "en"

class FlashcardCreate(FlashcardBase):
    pass

class Flashcard(FlashcardBase):
    id: int
    created_at: str

@router.post("/flashcards", response_model=Flashcard)
async def add_flashcard(flashcard: FlashcardCreate, db: Session = Depends(get_db)):
    """
    Create a new flashcard.
    """
    try:
        result = await create_flashcard(db=db, flashcard=flashcard)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/flashcards", response_model=List[Flashcard])
async def list_flashcards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all flashcards.
    """
    try:
        flashcards = await get_flashcards(db=db, skip=skip, limit=limit)
        return flashcards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/flashcards/{flashcard_id}", response_model=Flashcard)
async def get_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    """
    Get a specific flashcard by ID.
    """
    try:
        flashcard = await get_flashcard_by_id(db=db, flashcard_id=flashcard_id)
        if flashcard is None:
            raise HTTPException(status_code=404, detail="Flashcard not found")
        return flashcard
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/flashcards/{flashcard_id}", response_model=dict)
async def remove_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    """
    Delete a flashcard.
    """
    try:
        success = await delete_flashcard(db=db, flashcard_id=flashcard_id)
        if not success:
            raise HTTPException(status_code=404, detail="Flashcard not found")
        return {"success": True, "message": "Flashcard deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 