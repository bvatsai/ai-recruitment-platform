from dataclasses import dataclass
from datetime import date
from app.candidate.resume.resume_enums import EducationLevel, GradingSystem

@dataclass
class Education:
    education_level: EducationLevel
    qualification: str
    institution: str
    start_date: date
    end_date: date | None = None
    specialization: str | None = None
    score: float | None = None
    grading_system: GradingSystem | None = None

    def is_valid(self) -> bool:
        if self.start_date >= date.today():
            return False

        if self.end_date is None:
            return True

        return self.end_date > self.start_date
    
    def is_duplicate_of(self, other: "Education") -> bool:
        return (
            self.qualification.lower() == other.qualification.lower() and
            self.institution.lower() == other.institution.lower() and
            self.start_date == other.start_date
        )