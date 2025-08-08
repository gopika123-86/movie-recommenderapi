from fastapi import FastAPI
from app.routes import movie_routes
#, user_routes, recommendation_routes
from app.db import database

# Create FastAPI app instance
movieapp = FastAPI(title="Movie RecommendationS API")

# Initialize the database (e.g., create tables if they don't exist)
database.Base.metadata.create_all(bind=database.engine)

# Include routers from different modules
#app.include_router(user_routes.router, prefix="/users", tags=["Users"])
print("before movieapp called -------------------------")
#movieapp.include_router(movie_routes.router, prefix="/movies", tags=["Movies"])
movieapp.include_router(movie_routes.router)

#app.include_router(recommendation_routes.router, prefix="/recommendations",  tags=["Recommendations"])

