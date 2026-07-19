from enum import Enum

class applicationStatus(Enum):
    SUSPENDED = "Suspended"
    DELETED = "Deleted"
    WITHDRAWN = "Withdrawn"
    HIRED = "Hired"
    SCREENING = "Screening"
    INTERVIEWING = "Interviewing"
    REJECTED = "Rejected"
    APPLIED = "Applied"