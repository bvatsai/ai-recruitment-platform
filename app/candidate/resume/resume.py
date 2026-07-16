from dataclasses import dataclass, field

from app.candidate.resume.education import Education
from app.candidate.resume.experience import Experience
from app.candidate.resume.project import Project
from app.candidate.resume.certification import Certification
from app.candidate.resume.skill import Skill

@dataclass
class Resume:
    summary: str | None = None
    educations: list[Education] = field(default_factory=list)
    experiences: list[Experience] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)
    certifications: list[Certification] = field(default_factory=list)
    skills: list[Skill] = field(default_factory=list)

    def has_skill(self, skill_name: str) -> bool:
        return any(skill.name.lower() == skill_name.lower() for skill in self.skills)
    
    def add_skill(self, skill: Skill) -> bool:
        if not self.has_skill(skill.name):
            self.skills.append(skill)
            return True
        return False
    
    def remove_skill(self, skill: Skill) -> bool:
        if self.has_skill(skill.name):
            self.skills.remove(skill)
            return True
        return False