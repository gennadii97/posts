from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import (UserCreate, UserResponse)
from crud.crud import create_user, get_user_by_username
from app import get_async_session

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_new_user(user:UserCreate, db:Session = Depends(get_async_session)):
    existing_user = get_user_by_username(db,username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db=db, user=user)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id:int, db:Session=Depends(get_async_session)):
    pass
