from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.movie_routes import router as movie_router
from app.routes.recommendation_routes import router as recommendation_router

app = FastAPI(title="🎬 Movie Recommender API")

# Include routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(movie_router, prefix="/movies", tags=["Movies"])
app.include_router(recommendation_router, prefix="/recommendations", tags=["Recommendations"])
