from dataclasses import dataclass, field    #dataclass and field are decorators that simplify the creation of classes that are primarily used to store data.
from datetime import date                   #date is used to represent dates in the class.
from app.candidate.resume.project import Project    #project is imported from the app.candidate.resume.project module, which is used to represent a project in the Experience class.

@dataclass
class Experience:
    company_name: str
    designation: str
    start_date: date
    end_date: date | None = None
    tech_stack: list[str] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)