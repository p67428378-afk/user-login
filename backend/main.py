
from fastapi import FastAPI
from backend.api.v1 import premium_calculation
from backend.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vehicle Insurance Premium Calculator",
    description="An API to calculate vehicle insurance premiums based on various factors.",
    version="1.0.0"
)

app.include_router(premium_calculation.router, prefix="/api/v1/premium-calculation", tags=["Premium Calculation"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vehicle Insurance Premium Calculator API"}
