from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    post_id = Column(Integer, ForeignKey("posts.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_blocked = Column(Boolean, default=False)
    owner = relationship("User")
    post = relationship("Post")
