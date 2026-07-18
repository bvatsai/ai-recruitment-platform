from dataclasses import dataclass, field    #dataclass and field are decorators that simplify the creation of classes that are primarily used to store data.
from datetime import date                   #date is used to represent dates in the class.
from app.candidate.resume.resume_enums import OperationResult

from app.candidate.resume.project import Project    #project is imported from the app.candidate.resume.project module, which is used to represent a project in the Experience class.

@dataclass
class Experience:
    company: str                   #field must be provided when creating an instance of the Experience class.                    #field must be provided when creating an instance of the Experience class.
    start_date: date                    #field must be provided when creating an instance of the Experience class.
    designation: str | None = None
    end_date: date | None = None        #field is optional and can be left out when creating an instance of the Experience class. If not provided, it will default to None.
    tech_stack: list[str] = field(default_factory=list)     #field is of type object and can be optional and can be left out when creating an instance of the Experience class. If not provided, it will default to an empty list.
    projects: list[Project] = field(default_factory=list)   #field is of type object and can be optional and can be left out when creating an instance of the Experience class. If not provided, it will default to an empty list.

    def is_valid(self) -> bool:
        if self.start_date >= date.today():
            return False

        if self.end_date is None:
            return True

        return self.end_date > self.start_date
    
    def is_duplicate_of(self, other: "Experience") -> bool:
        return (
            self.company.lower() == other.company.lower() and
            self.start_date == other.start_date
        )
    
    def overlaps(self, other: "Experience") -> bool:
        if self.end_date is None:
            self.end_date = date.today()
        if other.end_date is None:
            other.end_date = date.today()
        if self.end_date is None and other.end_date is None:
            return False

        return not (self.end_date < other.start_date or self.start_date > other.end_date)