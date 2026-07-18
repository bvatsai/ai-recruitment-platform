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

    def is_duplicate_of(self, other: 'Project') -> bool:
        if self.start_date == other.start_date and self.project_name.lower() == other.project_name.lower():
            return True
        return False

    def is_valid(self) -> bool:
        if self.start_date >= date.today():
            return False

        if self.end_date is None:
            return True

        return self.end_date > self.start_date