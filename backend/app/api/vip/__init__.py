from fastapi import APIRouter

from app.api.vip import accent, writing, detection, humanize

router = APIRouter(prefix="/vip")

router.include_router(accent.router, tags=["accent"])
router.include_router(writing.router, tags=["writing"])
router.include_router(detection.router, tags=["detection"])
router.include_router(humanize.router, tags=["humanize"])
