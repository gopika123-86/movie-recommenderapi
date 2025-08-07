from pydantic import BaseModel, EmailStr
from typing import Optional




# ------------------------------
# User Schemas
# ------------------------------

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


# ------------------------------
# Movie Schemas
# ------------------------------

class MovieCreate(BaseModel):
    movie_name: str
    director: str
    movie_genre: str
    description: Optional[str] = None
    release_year: int

class MovieOut(BaseModel):
    id: int
    movie_name: str
    director: str
    movie_genre: str
    description: Optional[str]
    release_year: int

    class Config:
        orm_mode = True


# ------------------------------
# Rating Schemas
# ------------------------------

class RatingCreate(BaseModel):
    user_id: int
    movie_id: int
    rating: int
    review: Optional[str] = None

class RatingOut(BaseModel):
    id: int
    user_id: int
    movie_id: int
    rating: int
    review: Optional[str]

    class Config:
        orm_mode = True

