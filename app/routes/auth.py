## app/routes/auth.py
## IS 601 Module 13
## Evan Garvey

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User

router = APIRouter()

@router.post("/register")
def register(user_data: dict, db: Session = Depends(get_db)):
    try:
        user = User.register(db, user_data)
        db.commit()
        db.refresh(user)
        return {"message": "User registered successfully."}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login")
def login(credentials: dict, db: Session = Depends(get_db)):
    auth = User.authenticate(db, credentials["email"], credentials["password"])
    if not auth:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return auth
