from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    auto_reply_enabled = Column(Boolean, default=False)
    reply_delay = Column(Integer, default=60)  # time of delay for reply
