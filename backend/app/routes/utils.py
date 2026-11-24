from typing import Literal

from fastapi import APIRouter


router = APIRouter(prefix='/utils',tags=["utils"])

@router.get("/health-check")
def health_check() -> Literal[True]:
    return True
