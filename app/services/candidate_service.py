from uuid import UUID

from fastapi import HTTPException

from app.models import candidate
from app.repositories.candidate_repository import CandidateRepository   #jumps to the file app/repositories/candidate_repository.py and imports the CandidateRepository class defined in that file. This repository is responsible for managing the storage and retrieval of candidate data. It provides methods to save a candidate and retrieve all candidates from the repository.
from app.api.request_models.create_candidate_request import CreateCandidateRequest #jumps to the file app/api/request_models/create_candidate_request.py and imports the CreateCandidateRequest class defined in that file. This class is a Pydantic model that defines the structure and validation rules for the request body when creating a new candidate.
from app.api.response_models.candidate_response import CandidateResponse #jumps to the file app/api/response_models/candidate_response.py and imports the CandidateResponse class defined in that file. This class is a Pydantic model that defines the structure of the response when returning candidate data from the API.

class CandidateService:

    def __init__(self, repository: CandidateRepository): #Step5-Creates an instance of the CandidateRepository class, which is responsible for managing the storage and retrieval of candidate data. This repository will be used to save the newly created candidate.
        self.repository = repository

    def create_candidate(self, request: CreateCandidateRequest):
        # Create a new candidate using the request data
        candidate = request.to_candidate()      #method is called on the object which is received as an argument to the function create_candidate. This method converts the request data into a Candidate object, which represents a candidate entity in the system.
        #Find if candidate with same email already exists in the repository
        existing_candidate = self.repository.find_by_email(candidate.profile.email)  #method is called on the repository instance to check if a candidate with the same email already exists in the repository. It searches through the stored candidates and returns the existing candidate if found, or None if no candidate with the same email exists.
        if existing_candidate:      
            #Raise Exception if candidate with same email already exists in the repository
            raise HTTPException(status_code=409, detail="Candidate with this email already exists")
        # Save the candidate to the repository
        candidate = self.repository.save(candidate)
        return CandidateResponse.from_candidate(candidate)  #method is called on the CandidateResponse class, which is a Pydantic model that defines the structure of the response when returning candidate data from the API. This method converts the Candidate object into a CandidateResponse object, which can be returned as a response to the API request.
        
    def get_candidate_by_email(self, email: str):
        candidate = self.repository.find_by_email(email)
        if not candidate:
            raise HTTPException(status_code=404, detail="Candidate not found")
        return CandidateResponse.from_candidate(candidate)

    def get_all_candidates(self)-> list[CandidateResponse]:
        candidates = self.repository.get_all()
        return [CandidateResponse.from_candidate(candidate) for candidate in candidates]
    
    def get_candidate_by_id(self, candidate_id: UUID):
        candidate = self.repository.get_by_id(candidate_id)
        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found"
            )

        return CandidateResponse.from_candidate(candidate)