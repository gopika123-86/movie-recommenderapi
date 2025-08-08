from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String(255), nullable=False)
    director = Column(String(50), nullable=False)
    movie_genre = Column(String(20), nullable=False)
    description = Column(Text)
    release_year = Column(Integer)
