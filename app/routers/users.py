from typing import List
import re

from fastapi import APIRouter, Depends, HTTPException
from app.schemas import User, UserCreate
from sqlalchemy.orm import Session
from .. import crud
from ..dependencies import get_db

router = APIRouter()


@router.get("/users", response_model=List[User])
def get_users(db: Session = Depends(get_db)) -> List[User]:
    return crud.get_users(db)

@router.get("/users/{id}", response_model=User)
def get_user(id: int, db: Session = Depends(get_db)) -> User:
    pass

@router.put("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    mails = re.findall('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,7}', user.email)
    if mails == []:
        raise HTTPException(400, "Invalid email address")
    user_db = crud.get_user_by_email(db, user.email)
    if user_db:
        raise HTTPException(400, "Account with that email already exists")
    crud.create_user(db, user)
    return user.email
