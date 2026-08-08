from __future__ import annotations
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Profile(Base):                                                                        #this is a SQLAlchemy model class that represents a profile entity in the system. It inherits from the Base class, which is defined in the app/database/database.py file and serves as the base class for all SQLAlchemy models in the application. By inheriting from Base, the Profile class gains access to the necessary functionality for interacting with the database, such as mapping to tables and defining relationships between models.
    __tablename__ = "profile"                                                               #this is a class attribute that specifies the name of the database table associated with the Profile model. In this case, the table name is set to "profile". This attribute is used by SQLAlchemy to map the Profile class to the corresponding table in the database, allowing for CRUD operations and queries to be performed on the profile data.

    profile_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    candidate: Mapped["Candidate"] = relationship("Candidate", back_populates="profile")    #this is a relationship attribute that establishes a one-to-one relationship between the Profile model and the Candidate model. It allows for easy access to the associated candidate for a given profile. The relationship is defined using the relationship function from SQLAlchemy, specifying the target model as "Candidate" and using back_populates to indicate that the relationship is bidirectional, with the corresponding attribute in the Candidate model being named "profile". This enables navigation between profiles and their associated candidates in both directions.
    
    candidate_id: Mapped[UUID] = mapped_column(
        ForeignKey("candidate.candidate_id"),
        nullable=False,
        unique=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )