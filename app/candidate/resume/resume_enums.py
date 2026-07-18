from enum import Enum, auto

class OperationResult(Enum):
    SUCCESS = auto()
    ALREADY_EXISTS = auto()
    NOT_FOUND = auto()
    VALIDATION_FAILED = auto()
    CONFLICT = auto()

class ProficiencyLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    EXPERT = "Expert"

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