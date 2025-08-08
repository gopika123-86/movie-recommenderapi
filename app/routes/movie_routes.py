from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import MovieCreate, MovieOut
from app.models.models import Movie
from app.db.database import get_db

router = APIRouter()

#@router.post("/movies", response_model=MovieOut)
@router.post("/movies", response_model=MovieOut)
def create_movie(movieobj: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(**movieobj.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return MovieOut

#@router.get("/movies", response_model=list[MovieOut])
@router.get("/movies", response_model=None)
def get_movies(db: Session = Depends(get_db)):
    print(" get movies called -------------------------")
    return db.query(Movie).all()
