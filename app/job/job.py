from datetime import date
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from app.candidate.resume import Skill
from job.job_enum import JobMode, JobStatus, JobType, JobLevel, JobCategory    

def create_job_id() -> UUID:
    return uuid4()  

@dataclass
class Job:
    job_id: UUID = field(default_factory=create_job_id)  # Unique identifier for the job, generated using UUID.
    title: str
    description: str
    company_name: str
    location: str
    status: JobStatus
    job_type: JobType
    level: JobLevel
    requirements: str
    required_skills: list[Skill]
    min_experience_required: int
    max_experience_required: int
    category: JobCategory
    mode: JobMode
    min_salary: int
    max_salary: int
    posted_date: date
    closing_date: date | None = None

    def is_valid(self) -> bool:
        if self.posted_date > date.today():
            return False

        if self.closing_date is None:
            return True

        return self.closing_date > self.posted_date