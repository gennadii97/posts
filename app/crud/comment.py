from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate,CommentUpdate
from security import get_password_hash
from datetime import datetime



def create_comment(db: Session, comment: CommentCreate, owner_id: int):
    db_comment = Comment(
        content=comment.content,
        post_id=comment.post_id,
        owner_id=owner_id,
        created_at=datetime.utcnow(),
        is_blocked=False
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()


def get_comments_by_post(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()


def update_comment(db: Session, comment_id: int, comment_update: CommentUpdate):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not db_comment:
        return None
    if comment_update.content:
        db_comment.content = comment_update.content
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return True
    return False
