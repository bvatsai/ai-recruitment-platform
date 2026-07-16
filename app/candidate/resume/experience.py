from dataclasses import dataclass, field    #dataclass and field are decorators that simplify the creation of classes that are primarily used to store data.
from datetime import date                   #date is used to represent dates in the class.

from app.candidate.resume.project import Project    #project is imported from the app.candidate.resume.project module, which is used to represent a project in the Experience class.

@dataclass
class Experience:
    company_name: str                   #field must be provided when creating an instance of the Experience class.
    designation: str                    #field must be provided when creating an instance of the Experience class.
    start_date: date                    #field must be provided when creating an instance of the Experience class.
    end_date: date | None = None        #field is optional and can be left out when creating an instance of the Experience class. If not provided, it will default to None.
    tech_stack: list[str] = field(default_factory=list)     #field is of type object and can be optional and can be left out when creating an instance of the Experience class. If not provided, it will default to an empty list.
    projects: list[Project] = field(default_factory=list)   #field is of type object and can be optional and can be left out when creating an instance of the Experience class. If not provided, it will default to an empty list.