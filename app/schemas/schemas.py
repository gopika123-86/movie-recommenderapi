from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
#from app.db.database import get_db
#from app.schemas import MovieCreate, Movie

#app = FastAPI()

#database.Base.metadata.create_all(bind=database.engine)

#@app.post('/movies/', response_model=Movie)
#def create_movie(movie: MovieCreate, db: Session = Depends(database.get_db)):
#    db_movie = models.Movie(**movie.dict())
#    db.add(db_movie)
#   db.commit()
#    db.refresh(db_movie)
#    return db_movie
from pydantic import BaseModel

class MovieBase(BaseModel):
    id: int
    movie_name: str
    director: str
    movie_Genre: str
    description: str = None
    Release_year: int

class MovieCreate(MovieBase):
    pass

class MovieOut(MovieBase):
    pass

class UserBase(BaseModel):
    id: int
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    pass




#class Movie(MovieBase):
#    id: int

#    class Config:
#        orm_mode = True


