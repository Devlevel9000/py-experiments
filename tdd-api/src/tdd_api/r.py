from fastapi import APIRouter

from tdd_api.core.dependencies import Logger

router = APIRouter(prefix="/r", tags=["r"])


@router.get("")
async def test(log: Logger) -> dict[str, str]:
    return {"r": "r is called"}
