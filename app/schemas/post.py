from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=250)
    content: Optional[str] = Field(None)


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    owner_id: int
    created_at: datetime

