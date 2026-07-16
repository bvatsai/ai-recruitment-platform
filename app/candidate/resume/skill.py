from dataclasses import dataclass
from datetime import date
from enum import Enum

class ProficiencyLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    EXPERT = "Expert"

@dataclass
class Skill:
    name: str
    years_of_experience: float | None
    self_proficiency: ProficiencyLevel | None
    ai_proficiency: ProficiencyLevel | None
    last_used: date | None