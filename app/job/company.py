from dataclasses import dataclass,field
from uuid import UUID,uuid4

def create_company_id() -> UUID:
    return uuid4()

@dataclass
class Company:
    company_id: UUID = field(default_factory=create_company_id)
    name: str
    industry: str
    website: str | None = None
    headquarters: str | None = None
    logo_url: str | None = None

