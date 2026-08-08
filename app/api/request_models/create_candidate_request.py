from pydantic import BaseModel
from app.models.candidate import Candidate
from app.models.profile import Profile

class CreateCandidateRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None = None

    def to_candidate(self) -> Candidate:

        candidate = Candidate()

        profile = Profile(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone
        )
        candidate.profile = profile

        return candidate