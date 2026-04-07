from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uuid
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserLogin(UserBase):
    password: str

class UserOut(UserBase):
    id: uuid.UUID
    is_active: bool
    mfa_enabled: bool
    created_at: datetime
    updated_at: Optional[datetime]
    last_login_at: Optional[datetime]

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
