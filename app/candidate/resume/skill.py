from dataclasses import dataclass
from datetime import date
from enum import Enum
from app.candidate.resume.resume_enums import OperationResult, ProficiencyLevel

@dataclass
class Skill:
    name: str
    years_of_experience: float | None = None
    self_proficiency: ProficiencyLevel | None = None
    ai_proficiency: ProficiencyLevel | None = None
    last_used: int | None = None

    def has_skill(self, skill_name: str) -> OperationResult:
        return any(skill.name.lower() == skill_name.lower() for skill in self.skills)
    
    def is_duplicate_of(self, other: "Skill") -> bool:
        return self.name.lower() == other.name.lower()  