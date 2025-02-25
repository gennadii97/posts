from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    auto_reply_enabled: Optional[bool] = Field(default=False)
    reply_delay: Optional[int] = Field(default=60, ge=0)


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    auto_reply_enabled: bool
    reply_delay: int

