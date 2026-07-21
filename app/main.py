from fastapi import FastAPI
from app.api.routers.candidate_router import router as candidate_router #jumps to the file app/api/routers/candidate_router.py and imports the router instance defined in that file. This router contains all the candidate-related endpoints, such as creating a candidate, retrieving candidates, etc.

app = FastAPI()                         #Creates a FastAPI instance which is the main entry point for the application. This instance will be used to define routes, middleware, and other configurations for the API.

app.include_router(candidate_router)    #Includes Router for candidate endpoints which is file app/api/routers/candidate_router.py. This router handles all the candidate-related endpoints, such as creating a candidate, retrieving candidates, etc.

@app.get("/")
def root():
    return {"message": "Welcome to Enterprise AI Recruitment Platform"}