from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from app.application.application_enum import applicationStatus

def create_application_id() -> UUID:
    return uuid4()

@dataclass
class Application:
    application_id: UUID = field(default_factory=create_application_id)
    candidate_id: UUID
    job_id: UUID
    status: applicationStatus
    updated_at: datetime = field(default_factory=datetime.now)
    application_date: datetime = field(default_factory=datetime.now)

    def touch(self) -> None:
        self.updated_at = datetime.now()

    def is_valid(self) -> bool:
        return self.application_date <= datetime.now() and self.status in applicationStatus
    
    def is_duplicate_of(self, other: "Application") -> bool:
        return self.candidate_id == other.candidate_id and self.job_id == other.job_id