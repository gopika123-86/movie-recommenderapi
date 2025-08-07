# app/models/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    ratings = relationship("Rating", back_populates="user")

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String(255), nullable=False)
    director = Column(String(50), nullable=False)
    movie_genre = Column(String(20), nullable=False)
    description = Column(Text)
    release_year = Column(Integer)

    ratings = relationship("Rating", back_populates="movie")

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text)

    __table_args__ = (
        CheckConstraint('rating BETWEEN 1 AND 5'),
    )

    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")
