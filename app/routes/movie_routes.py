from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import MovieCreate, MovieOut
from app.models.models import Movie
from app.db.database import get_db

router = APIRouter()

@router.post("/movies", response_model=MovieOut)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@router.get("/movies", response_model=list[MovieOut])
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()
