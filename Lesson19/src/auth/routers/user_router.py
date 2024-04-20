from fastapi import APIRouter
from src.auth.schemas.user_schema import User




router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)


@router.post("")
def data_actor_validated(user: User) -> User:
    return user
