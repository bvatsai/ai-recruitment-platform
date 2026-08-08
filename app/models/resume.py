from __future__ import annotations
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Resume(Base):                                     #this is a SQLAlchemy model class that represents a resume entity in the system. It inherits from the Base class, which is defined in the app/database/database.py file and serves as the base class for all SQLAlchemy models in the application. By inheriting from Base, the Resume class gains access to the necessary functionality for interacting with the database, such as mapping to tables and defining relationships between models.
    __tablename__ = "resume"                            #this is a class attribute that specifies the name of the database table associated with the Resume model. In this case, the table name is set to "resume". This attribute is used by SQLAlchemy to map the Resume class to the corresponding table in the database, allowing for CRUD operations and queries to be performed on the resume data.

    resume_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    candidate_id: Mapped[UUID] = mapped_column(
        ForeignKey("candidate.candidate_id"),
        nullable=False,
        unique=True
    )

    extracted_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    candidate: Mapped["Candidate"] = relationship(      #this is a relationship attribute that establishes a one-to-one relationship between the Resume model and the Candidate model. It allows for easy access to the associated candidate for a given resume. The relationship is defined using the relationship function from SQLAlchemy, specifying the target model as "Candidate" and using back_populates to indicate that the relationship is bidirectional, with the corresponding attribute in the Candidate model being named "resume". This enables navigation between resumes and their associated candidates in both directions.
        "Candidate",
        back_populates="resume"
    )

    file_path: Mapped[str] = mapped_column(
    String(500),
    nullable=False
)