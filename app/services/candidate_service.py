from app.repositories.candidate_repository import CandidateRepository   #jumps to the file app/repositories/candidate_repository.py and imports the CandidateRepository class defined in that file. This repository is responsible for managing the storage and retrieval of candidate data. It provides methods to save a candidate and retrieve all candidates from the repository.
from app.api.request_models.create_candidate_request import CreateCandidateRequest #jumps to the file app/api/request_models/create_candidate_request.py and imports the CreateCandidateRequest class defined in that file. This class is a Pydantic model that defines the structure and validation rules for the request body when creating a new candidate.
from app.api.response_models.candidate_response import CandidateResponse #jumps to the file app/api/response_models/candidate_response.py and imports the CandidateResponse class defined in that file. This class is a Pydantic model that defines the structure of the response when returning candidate data from the API.

class CandidateService:

    def __init__(self): 
        self.repository = CandidateRepository() #Step5-Creates an instance of the CandidateRepository class, which is responsible for managing the storage and retrieval of candidate data. This repository will be used to save the newly created candidate.
                                                #Till step 5 everything is in Memory before we click POST
    def create_candidate(self, request: CreateCandidateRequest):
        # Create a new candidate using the request data
        candidate = request.to_candidate()      #method is called on the object which is received as an argument to the function create_candidate. This method converts the request data into a Candidate object, which represents a candidate entity in the system.
        # Save the candidate to the repository
        self.repository.save(candidate)
        return CandidateResponse.from_candidate(candidate)  #method is called on the CandidateResponse class, which is a Pydantic model that defines the structure of the response when returning candidate data from the API. This method converts the Candidate object into a CandidateResponse object, which can be returned as a response to the API request.