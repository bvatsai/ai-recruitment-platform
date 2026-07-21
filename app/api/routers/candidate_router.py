from fastapi import APIRouter   #jumps to the file fastapi/APIRouter.py and imports the APIRouter class defined in that file. This class is used to create a router instance that can be used to define and group related endpoints together. In this case, it will be used for candidate-related endpoints.
from app.services.candidate_service import CandidateService #jumps to the file app/services/candidate_service.py and imports the CandidateService class defined in that file. This service contains the business logic for handling candidate-related operations, such as creating a candidate, retrieving candidates, etc.
from app.api.request_models.create_candidate_request import CreateCandidateRequest  #jumps to the file app/api/request_models/create_candidate_request.py and imports the CreateCandidateRequest class defined in that file. This class is a Pydantic model that defines the structure and validation rules for the request body when creating a new candidate.

router = APIRouter(             #Step3-Defines a new APIRouter instance which is used to group related endpoints together. In this case, it will be used for candidate-related endpoints.
    prefix="/candidates",
    tags=["Candidates"]
)

candidate_service = CandidateService()  #Step4-Creates an instance of the CandidateService class, which contains the business logic for handling candidate-related operations. This service will be used in the endpoint to create a new candidate.

@router.post("")
def create_candidate(request: CreateCandidateRequest):  #This is where FAST API takes the Input and creates an instance of CreateCandidateRequest class and then passes it to the function create_candidate as an argument. The function then uses this request object to create a new candidate.
                                                        #Also, on the Docs page you would see a default JSON body suggesting what fields are required to create a candidate. This is because the CreateCandidateRequest class is a Pydantic model that defines the structure and validation rules for the request body when creating a new candidate. FastAPI uses this model to automatically generate the request body schema and provide it in the API documentation.
    candidate = candidate_service.create_candidate(request)
    return candidate
