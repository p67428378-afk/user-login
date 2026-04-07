from sqlalchemy.orm import Session
from backend import models, schemas
from backend.auth import get_password_hash
from sqlalchemy.sql import func

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_last_login(db: Session, user: models.User):
    user.last_login_at = func.now()
    db.commit()
    db.refresh(user)
    return user
