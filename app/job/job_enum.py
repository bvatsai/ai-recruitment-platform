from enum import Enum

class JobStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"
    DELETED = "Deleted"


class JobType(Enum):
    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"
    CONTRACT = "Contract"
    INTERNSHIP = "Internship"


class JobMode(Enum):
    REMOTE = "Remote"
    ONSITE = "Onsite"
    HYBRID = "Hybrid"


class JobLevel(Enum):
    JUNIOR = "Junior"
    MID_LEVEL = "Mid Level"
    SENIOR = "Senior"
    LEAD = "Lead"


class JobCategory(Enum):
    TECHNOLOGY = "Technology"
    MARKETING = "Marketing"
    SALES = "Sales"
    HUMAN_RESOURCES = "Human Resources"