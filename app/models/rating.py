from sqlalchemy import Column, Integer, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.db import Base

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text)

    __table_args__ = (
        CheckConstraint('rating BETWEEN 1 AND 5'),
    )

    user = relationship('User', back_populates='ratings')
    movie = relationship('Movie', back_populates='ratings')