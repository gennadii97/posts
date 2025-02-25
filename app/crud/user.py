from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.utils import generate_passwd_hash


async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()


async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalars().first()


async def create_user(session: AsyncSession, user: UserCreate):
    hashed_password = generate_passwd_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def update_user(session: AsyncSession, user_id: int, user_update: UserUpdate):
    result = await session.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if not db_user:
        return None
    if user_update.auto_reply_enabled is not None:
        db_user.auto_reply_enabled = user_update.auto_reply_enabled
    if user_update.reply_delay is not None:
        db_user.reply_delay = user_update.reply_delay
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def delete_user(session: AsyncSession, user_id: int):
    result = await  session.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user:
        await session.delete(db_user)
        await session.commit()
        return True
    return False
