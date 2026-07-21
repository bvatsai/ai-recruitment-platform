from dataclasses import dataclass

@dataclass
class Profile:
    email: str  # Non Default fields should always be mentioned first
    first_name: str
    last_name: str
    phone: str | None = None
    location: str | None = None
    linkedin_url: str | None = None