from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from app.db.models.flashcard import Flashcard

class FlashcardCreate(BaseModel):
    front: str
    back: str
    context: Optional[str] = None
    language: str = "en"

async def create_flashcard(db: Session, flashcard: FlashcardCreate):
    """
    Create a new flashcard.
    """
    db_flashcard = Flashcard(
        front=flashcard.front,
        back=flashcard.back,
        context=flashcard.context,
        language=flashcard.language
    )
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)
    
    # Convert SQLAlchemy model to dict for response
    return {
        "id": db_flashcard.id,
        "front": db_flashcard.front,
        "back": db_flashcard.back,
        "context": db_flashcard.context,
        "language": db_flashcard.language,
        "created_at": db_flashcard.created_at.isoformat() if db_flashcard.created_at else None
    }

async def get_flashcards(db: Session, skip: int = 0, limit: int = 100):
    """
    Get all flashcards.
    """
    flashcards = db.query(Flashcard).offset(skip).limit(limit).all()
    
    # Convert SQLAlchemy models to dicts for response
    return [
        {
            "id": fc.id,
            "front": fc.front,
            "back": fc.back,
            "context": fc.context,
            "language": fc.language,
            "created_at": fc.created_at.isoformat() if fc.created_at else None
        }
        for fc in flashcards
    ]

async def get_flashcard_by_id(db: Session, flashcard_id: int):
    """
    Get a specific flashcard by ID.
    """
    flashcard = db.query(Flashcard).filter(Flashcard.id == flashcard_id).first()
    
    if not flashcard:
        return None
    
    # Convert SQLAlchemy model to dict for response
    return {
        "id": flashcard.id,
        "front": flashcard.front,
        "back": flashcard.back,
        "context": flashcard.context,
        "language": flashcard.language,
        "created_at": flashcard.created_at.isoformat() if flashcard.created_at else None
    }

async def delete_flashcard(db: Session, flashcard_id: int):
    """
    Delete a flashcard.
    """
    flashcard = db.query(Flashcard).filter(Flashcard.id == flashcard_id).first()
    
    if not flashcard:
        return False
    
    db.delete(flashcard)
    db.commit()
    
    return True 