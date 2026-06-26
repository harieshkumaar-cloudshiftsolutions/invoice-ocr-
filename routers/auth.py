from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user import UserRegister, UserResponse
from services.auth_service import register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(db, user)