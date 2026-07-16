from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

from app.candidate.profile import Profile
from app.candidate.resume.resume import Resume

class CandidateStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"
    DELETED = "Deleted"

def create_candidate_id() -> UUID:  #"-> UUID" reprsents Object type hinting that the function returns a UUID object. The function will still work even if we don't include this type hint, but it can be helpful for documentation and code analysis tools.
    return uuid4()                  

def create_profile() -> Profile:
    return Profile()

def create_resume() -> Resume:
    return Resume()

@dataclass
class Candidate:
    candidate_id: UUID = field(default_factory=create_candidate_id) #function create_candidate_id is called to generate a new UUID for the candidate_id field when a new instance of the Candidate class is created. This ensures that each candidate has a unique identifier.
    profile: Profile = field(default_factory=create_profile)        #function create_profile is called to generate a new Profile object for the profile field when a new instance of the Candidate class is created.
    resume: Resume = field(default_factory=create_resume)           #function create_resume is called to generate a new Resume object for the resume field when a new instance of the Candidate class is created.
    status: CandidateStatus = CandidateStatus.ACTIVE
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

