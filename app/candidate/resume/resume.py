from dataclasses import dataclass, field

from app.candidate.resume import experience
from app.candidate.resume.education import Education
from app.candidate.resume.experience import Experience
from app.candidate.resume.project import Project
from app.candidate.resume.certification import Certification
from app.candidate.resume.skill import Skill
from app.candidate.resume.resume_enums import OperationResult

@dataclass
class Resume:
    summary: str | None = None
    educations: list[Education] = field(default_factory=list)
    experiences: list[Experience] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)
    certifications: list[Certification] = field(default_factory=list)
    skills: list[Skill] = field(default_factory=list)

    
    def add_skill(self, skill: Skill) -> OperationResult:
        for existing_skill in self.skills:
            if existing_skill.is_duplicate_of(skill):
                return OperationResult.ALREADY_EXISTS
        self.skills.append(skill)
        return OperationResult.SUCCESS

    def remove_skill(self, skill: Skill) -> OperationResult:
        if self.has_skill(skill.name):
            self.skills.remove(skill)
            return OperationResult.SUCCESS
        return OperationResult.NOT_FOUND
    
    def add_experience(self, experience: Experience) -> OperationResult:
        if not experience.is_valid():
            return OperationResult.VALIDATION_FAILED
        for existing_experience in self.experiences:
            if existing_experience.is_duplicate_of(experience):
                return OperationResult.ALREADY_EXISTS
            if existing_experience.overlaps(experience):
                return OperationResult.CONFLICT
        self.experiences.append(experience)
        return OperationResult.SUCCESS

    def remove_experience(self, experience: Experience) -> OperationResult:
        if experience in self.experiences:      #as we have experience defined as a dataclass, we can use the 'in' operator to check if the experience exists in the list of experiences by checking values and not references. If it does, we remove it and return SUCCESS. If it doesn't, we return NOT_FOUND.
            self.experiences.remove(experience)
            return OperationResult.SUCCESS
        return OperationResult.NOT_FOUND
    
    def add_project(self, project: Project) -> OperationResult:
        if not project.is_valid():
            return OperationResult.VALIDATION_FAILED
        for existing_project in self.projects:
            if existing_project.is_duplicate_of(project):
                return OperationResult.ALREADY_EXISTS
        self.projects.append(project)
        return OperationResult.SUCCESS

    def remove_project(self, project: Project) -> OperationResult:
        if project in self.projects:
            self.projects.remove(project)
            return OperationResult.SUCCESS
        return OperationResult.NOT_FOUND
    
    def add_education(self, education: Education) -> OperationResult:
        if not education.is_valid():
            return OperationResult.VALIDATION_FAILED
        for existing_education in self.educations:
            if existing_education.is_duplicate_of(education):
                return OperationResult.ALREADY_EXISTS
        self.educations.append(education)
        return OperationResult.SUCCESS
    
    def remove_education(self, education: Education) -> OperationResult:
        if education in self.educations:
            self.educations.remove(education)
            return OperationResult.SUCCESS
        return OperationResult.NOT_FOUND
    
    def add_certification(self, certification: Certification) -> OperationResult:
        if not certification.is_valid():
            return OperationResult.VALIDATION_FAILED
        for existing_certification in self.certifications:
            if existing_certification.is_duplicate_of(certification):
                return OperationResult.ALREADY_EXISTS
        self.certifications.append(certification)
        return OperationResult.SUCCESS
    
    def remove_certification(self, certification: Certification) -> OperationResult:
        if certification in self.certifications:
            self.certifications.remove(certification)
            return OperationResult.SUCCESS
        return OperationResult.NOT_FOUND
    