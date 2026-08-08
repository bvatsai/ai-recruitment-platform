from app.models.candidate import Candidate   #jumps to the file app/candidate/candidate.py and imports the Candidate class defined in that file. This class represents a candidate entity in the system, containing attributes such as candidate_id, profile, and resume. It serves as a data model for candidates and is used throughout the application to manage candidate-related operations.
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.profile import Profile

class CandidateRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, candidate: Candidate):
        self.session.add(candidate)
        self.session.commit()
        self.session.refresh(candidate)

        return candidate

    def get_all(self) -> list[Candidate]:
        return self.session.query(Candidate).all()
    
    def find_by_email(self, email: str):
        return (
        self.session.query(Candidate)
        .join(Profile)
        .filter(Profile.email == email)
        .first()
    )

    def get_by_id(self, candidate_id: UUID):
        return (
        self.session.query(Candidate)
        .filter(Candidate.candidate_id == candidate_id)
        .first()
    )