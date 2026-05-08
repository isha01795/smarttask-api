from fastapi import APIRouter, Depends
from app.core.deps import get_current_user

router = APIRouter(prefix="/protected", tags=["Protected"])


@router.get("/me")
def read_me(user_id: int = Depends(get_current_user)):
    return {"user_id": user_id}