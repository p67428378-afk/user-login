from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend import crud, schemas, auth
from backend.database import get_db
from backend.config import settings

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Annotated[Session, Depends(get_db)]):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]):
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user or not crud.verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=schemas.UserOut)
async def read_users_me(current_user: Annotated[schemas.UserOut, Depends(auth.get_current_user)]):
    return current_user
