from dataclasses import dataclass

@dataclass
class Certification:
    name: str
    issuing_organization: str
    issue_date: str
    expiration_date: str | None
    credential_id: str | None
    credential_url: str | None