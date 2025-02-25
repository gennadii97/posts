from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import user
from app.schemas.user import UserBase, UserCreate, UserResponse
from app.database import db_helper

router = APIRouter(tags=["Users"])


@router.get("/users/{users_id}")
async def read_user_endpoint(user_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await user.get_user(session, user_id=user_id)


@router.post("/users")
async def create_user_endpoint(usr: UserCreate, db: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await user.create_user(db, user=usr)
