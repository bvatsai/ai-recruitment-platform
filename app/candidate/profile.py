from dataclasses import dataclass

@dataclass
class Profile:
    email: str  # Non Default fields should always be mentioned first
    name: str | None = None
    phone: str | None = None
    location: str | None = None
    linkedin_url: str | None = None