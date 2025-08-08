from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import UserCreate, UserOut
from app.models.models import User
from app.db.database import get_db


router = APIRouter()

#@router.post("/users", response_model=UserOut)
@router.post("/users", response_model=None)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or Email already registered")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserCreate

#@router.get("/users", response_model=list[UserOut])
@router.get("/users", response_model=None)
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
