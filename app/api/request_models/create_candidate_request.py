from pydantic import BaseModel
from app.candidate.candidate import Candidate
from app.candidate.profile import Profile

class CreateCandidateRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None = None

    def to_candidate(self) -> 'Candidate':       

        TempProfile = Profile(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone
        )
        return Candidate(profile=TempProfile)   #Candidate object is created with the profile object created above. The Candidate class has a field named profile which is of type Profile. When creating a new instance of the Candidate class, we need to provide a Profile object for this field. In this case, we are passing the profile object that we just created using the data from the CreateCandidateRequest instance. This allows us to create a new Candidate instance with the provided profile information.
                                                #Also, as it creates Candidate Object, it automatically generates a unique candidate_id and creates a new Resume object for the resume field using the default_factory functions defined in the Candidate class.