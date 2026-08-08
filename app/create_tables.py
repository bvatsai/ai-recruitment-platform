from app.database.database import Base, engine

from app.models.candidate import Candidate
from app.models.profile import Profile
from app.models.resume import Resume

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")