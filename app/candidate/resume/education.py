from dataclasses import dataclass
from datetime import date
from enum import Enum

class EducationLevel(Enum):
    SECONDARY = "Secondary"
    HIGHER_SECONDARY = "Higher Secondary"
    BACHELORS = "Bachelor's"
    MASTERS = "Master's"
    DOCTORATE = "Doctorate"

class GradingSystem(Enum):
    PERCENTAGE = "Percentage"
    CGPA = "CGPA"
    GPA = "GPA"
    GRADE = "Grade"

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