from __future__ import annotations
from cProfile import Profile
from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base

class Candidate(Base):                                                                                  #this is a SQLAlchemy model class that represents a candidate entity in the system. It inherits from the Base class, which is defined in the app/database/database.py file and serves as the base class for all SQLAlchemy models in the application. By inheriting from Base, the Candidate class gains access to the necessary functionality for interacting with the database, such as mapping to tables and defining relationships between models.
    __tablename__ = "candidate"

    profile: Mapped["Profile"] = relationship("Profile",uselist=False, back_populates="candidate")      #this is a relationship attribute that establishes a one-to-one relationship between the Candidate model and the Profile model. It allows for easy access to the associated profile for a given candidate. The relationship is defined using the relationship function from SQLAlchemy, specifying the target model as "Profile" and using back_populates to indicate that the relationship is bidirectional, with the corresponding attribute in the Profile model being named "candidate". This enables navigation between candidates and their associated profiles in both directions.

    resume: Mapped["Resume"] = relationship("Resume",back_populates="candidate", uselist=False)         #this is a relationship attribute that establishes a one-to-one relationship between the Candidate model and the Resume model. It allows for easy access to the associated resume for a given candidate. The relationship is defined using the relationship function from SQLAlchemy, specifying the target model as "Resume" and using back_populates to indicate that the relationship is bidirectional, with the corresponding attribute in the Resume model being named "candidate". This enables navigation between candidates and their associated resumes in both directions.
        
    candidate_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="ACTIVE"
    )