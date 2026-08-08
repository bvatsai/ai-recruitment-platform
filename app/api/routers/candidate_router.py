from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_session
from app.repositories.candidate_repository import CandidateRepository
from app.services.candidate_service import CandidateService
from app.api.request_models.create_candidate_request import CreateCandidateRequest

router = APIRouter(             #Step3-Defines a new APIRouter instance which is used to group related endpoints together. In this case, it will be used for candidate-related endpoints.
    prefix="/candidates",
    tags=["Candidates"]
)

@router.post("")
def create_candidate(
    request: CreateCandidateRequest,            #Defines a new endpoint for creating a candidate. This endpoint listens for POST requests at the "/candidates" URL. It takes a request body of type CreateCandidateRequest, which is a Pydantic model that defines the structure and validation rules for the request body when creating a new candidate.
    session: Session = Depends(get_session)     #This is dependency injection. It tells FastAPI: "Before calling create_candidate(), I need a Session. To get one, call get_session()." this method is defined in the file app/database/database.py. It is a generator function that provides a database session to the caller. It creates a new session using the SessionLocal class, which is a session factory configured with the database engine. The session is yielded to the caller, allowing them to perform database operations within a context. After the caller is done using the session, it is closed in the finally block to ensure proper cleanup and release of resources.
):                                              #This is where FAST API takes the Input and creates an instance of CreateCandidateRequest class and then passes it to the function create_candidate as an argument. The function then uses this request object to create a new candidate.
                                                #Also, on the Docs page you would see a default JSON body suggesting what fields are required to create a candidate. This is because the CreateCandidateRequest class is a Pydantic model that defines the structure and validation rules for the request body when creating a new candidate. FastAPI uses this model to automatically generate the request body schema and provide it in the API documentation.
    repository = CandidateRepository(session)   #Creates an instance of the CandidateRepository class, which is responsible for managing the storage and retrieval of candidate data. This repository will be used to save the newly created candidate.
    service = CandidateService(repository)      #Creates an instance of the CandidateService class, which is responsible for handling the business logic related to candidates. This service will be used to create the new candidate using the request data.
    return service.create_candidate(request)    #This step calls the create_candidate method of the CandidateService class, passing in the request object. The service will handle the business logic of creating a new candidate, including checking for existing candidates with the same email and saving the new candidate to the repository. The result of this operation is returned as the response to the API request.


@router.get("/email/{email}")
def get_candidate_by_email(
    email: str,
    session: Session = Depends(get_session)
):
    repository = CandidateRepository(session)
    service = CandidateService(repository)
    return service.get_candidate_by_email(email)


@router.get("")
def get_all_candidates(
    session: Session = Depends(get_session)
):
    repository = CandidateRepository(session)
    service = CandidateService(repository)
    return service.get_all_candidates()

@router.get("/{candidate_id}")
def get_candidate_by_id(
    candidate_id: UUID,
    session: Session = Depends(get_session)
):
    repository = CandidateRepository(session)
    service = CandidateService(repository)

    return service.get_candidate_by_id(candidate_id)