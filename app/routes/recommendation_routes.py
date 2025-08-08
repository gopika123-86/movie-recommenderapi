from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.models import Rating, Movie
from app.schemas.schemas import MovieOut
from app.db.database import get_db

router = APIRouter()

#@router.get("/recommendations", response_model=list[MovieOut])
@router.get("/recommendations", response_model=None)
def get_recommendations(db: Session = get_db()):
    subquery = (
        db.query(
            Rating.movie_id,
            func.avg(Rating.rating).label("avg_rating")
        )
        .group_by(Rating.movie_id)
        .subquery()
    )

    movies = (
        db.query(Movie)
        .join(subquery, Movie.id == subquery.c.movie_id)
        .order_by(subquery.c.avg_rating.desc())
        .limit(5)
        .all()
    )

    return movies
