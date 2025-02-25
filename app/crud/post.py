from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostUpdate, PostCreate
from security import get_password_hash
from datetime import datetime


def create_post(db: Session, post: PostCreate, owner_id: int):
    db_post = Post(title=post.title, content=post.content, owner_id=owner_id, created_at=datetime.utcnow())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def get_posts_by_user(db: Session, owner_id: int):
    return db.query(Post).filter(Post.owner_id == owner_id).all()


def update_post(db: Session, post_id: int, post_update: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        return None
    if post_update.title:
        db_post.title = post_update.title
    if post_update.content:
        db_post.content = post_update.content
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return True
    return False
