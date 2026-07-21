from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from app.candidate.profile import Profile
from app.candidate.resume.resume import Resume
import app.candidate.candidate_enums as candidate_enums

def create_candidate_id() -> UUID:  #"-> UUID" reprsents Object type hinting that the function returns a UUID object. The function will still work even if we don't include this type hint, but it can be helpful for documentation and code analysis tools.
    return uuid4()                  

def create_profile() -> Profile:
    return Profile()

def create_resume() -> Resume:
    return Resume()

@dataclass
class Candidate:
    profile: Profile    #here we have not provided a default value for the profile field because for creating a candidate, profile needs to be created first and Profile has 3 mandatory fields and hence cannot just be assigned Default value, which means that when creating a new instance of the Candidate class, you must provide a Profile object for this field containing those 3 mandatory values. If you don't provide a Profile object, Python will raise a TypeError.
    candidate_id: UUID = field(default_factory=create_candidate_id) #function create_candidate_id is called to generate a new UUID for the candidate_id field when a new instance of the Candidate class is created. This ensures that each candidate has a unique identifier.
    resume: Resume = field(default_factory=create_resume)           #function create_resume is called to generate a new Resume object for the resume field when a new instance of the Candidate class is created.
    status: candidate_enums.CandidateStatus = candidate_enums.CandidateStatus.ACTIVE
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def touch(self) -> None:
        self.updated_at = datetime.now()