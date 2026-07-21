from uuid import UUID
from pydantic import BaseModel

from app.candidate.candidate import Candidate


class CandidateResponse(BaseModel):
    candidate_id: UUID
    first_name: str
    last_name: str
    email: str
    phone: str | None = None

    @classmethod
    def from_candidate(cls, candidate: Candidate) -> "CandidateResponse":
        return cls(
            candidate_id=candidate.candidate_id,
            first_name=candidate.profile.first_name,
            last_name=candidate.profile.last_name,
            email=candidate.profile.email,
            phone=candidate.profile.phone
        )