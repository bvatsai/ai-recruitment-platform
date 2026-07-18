from dataclasses import dataclass

@dataclass
class Certification:
    name: str
    issuing_organization: str
    issue_date: str
    expiration_date: str | None
    credential_id: str | None
    credential_url: str | None

    def is_valid(self) -> bool:
        if self.expiration_date is not None and self.expiration_date < self.issue_date:
            return False
        return True

    def is_duplicate_of(self, other: "Certification") -> bool:
        return (
            self.name.casefold() == other.name.casefold() and
            self.issuing_organization.casefold() == other.issuing_organization.casefold() and
            self.issue_date == other.issue_date
        )
    