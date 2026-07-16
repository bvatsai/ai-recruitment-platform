from dataclasses import dataclass
from datetime import date

@dataclass
class Project:
    project_name          : str
    description           : str
    role                  : str
    responsibilities      : str
    achievements          : str
    start_date            : date
    end_date              : date | None
    tech_stack            : list[str]
    team_size             : int | None