from typing import List

from fastapi import APIRouter
from app.schemas import User, UserCreate


router = APIRouter()


@router.get("/users", response_model=List[User])
def get_users() -> List[User]:
    pass

@router.get("/users/{id}", response_model=User)
def get_user(id: int) -> User:
    pass

@router.post("/create_user")
def create_user(user: UserCreate):
    pass