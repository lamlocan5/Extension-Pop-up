import pytest
from sqlalchemy.orm import Session

from app.db.models.flashcard import Flashcard
from app.services.flashcards import create_flashcard, get_flashcards, get_flashcard_by_id, delete_flashcard

@pytest.mark.asyncio
async def test_create_flashcard(db: Session):
    """
    Test creating a flashcard.
    """
    class FlashcardCreate:
        front = "Hello"
        back = "Hola"
        context = "Basic greeting"
        language = "es"
    
    flashcard = await create_flashcard(db, FlashcardCreate())
    
    assert flashcard["front"] == "Hello"
    assert flashcard["back"] == "Hola"
    assert flashcard["context"] == "Basic greeting"
    assert flashcard["language"] == "es"
    assert "id" in flashcard
    assert "created_at" in flashcard

@pytest.mark.asyncio
async def test_get_flashcards(db: Session):
    """
    Test retrieving all flashcards.
    """
    # Create some test flashcards
    class FlashcardCreate:
        def __init__(self, front, back):
            self.front = front
            self.back = back
            self.context = None
            self.language = "en"
    
    await create_flashcard(db, FlashcardCreate("Apple", "Manzana"))
    await create_flashcard(db, FlashcardCreate("Dog", "Perro"))
    
    flashcards = await get_flashcards(db)
    
    assert len(flashcards) >= 2  # There might be more from previous tests
    
    # Verify the recently added flashcards exist
    fronts = [fc["front"] for fc in flashcards]
    assert "Apple" in fronts
    assert "Dog" in fronts

@pytest.mark.asyncio
async def test_get_flashcard_by_id(db: Session):
    """
    Test retrieving a flashcard by ID.
    """
    class FlashcardCreate:
        front = "Book"
        back = "Libro"
        context = None
        language = "es"
    
    created = await create_flashcard(db, FlashcardCreate())
    
    retrieved = await get_flashcard_by_id(db, created["id"])
    
    assert retrieved is not None
    assert retrieved["id"] == created["id"]
    assert retrieved["front"] == "Book"
    assert retrieved["back"] == "Libro"

@pytest.mark.asyncio
async def test_delete_flashcard(db: Session):
    """
    Test deleting a flashcard.
    """
    class FlashcardCreate:
        front = "Delete Me"
        back = "Bórrame"
        context = None
        language = "es"
    
    created = await create_flashcard(db, FlashcardCreate())
    
    # Confirm it exists
    retrieved = await get_flashcard_by_id(db, created["id"])
    assert retrieved is not None
    
    # Delete it
    deleted = await delete_flashcard(db, created["id"])
    assert deleted is True
    
    # Confirm it's gone
    retrieved_after_delete = await get_flashcard_by_id(db, created["id"])
    assert retrieved_after_delete is None
    
    # Try deleting non-existent flashcard
    deleted_non_existent = await delete_flashcard(db, 9999)
    assert deleted_non_existent is False 