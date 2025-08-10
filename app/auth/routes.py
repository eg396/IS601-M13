# app/auth/routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.models.user import User
from app.database import get_db
from app.auth.jwt import get_current_user 

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = User.register(db, user_data.model_dump())
        db.commit()
        db.refresh(user)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    auth = User.authenticate(db, user_data.username, user_data.password)
    if not auth:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {
        "access_token": auth["access_token"],
        "refresh_token": auth["refresh_token"],
        "token_type": auth["token_type"],
        "expires_at": auth["expires_at"],
        "user": auth["user"],
    }

@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user