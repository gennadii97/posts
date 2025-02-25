from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    post_id: int


class CommentUpdate(BaseModel):
    content: Optional[str] = Field(None, max_length=500)


class CommentResponse(CommentBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    post_id: int
    owner_id: int
    created_at: datetime
    is_blocked: bool
