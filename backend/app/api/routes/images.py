from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.images import search_images

router = APIRouter()

class ImageSearchRequest(BaseModel):
    query: str
    count: int = 5

class ImageResult(BaseModel):
    url: str
    thumbnail_url: str
    alt_text: str

class ImageSearchResponse(BaseModel):
    results: List[ImageResult]

@router.post("/images", response_model=ImageSearchResponse)
async def find_images(request: ImageSearchRequest):
    """
    Search for images related to the query.
    """
    try:
        results = await search_images(
            query=request.query,
            count=request.count
        )
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 