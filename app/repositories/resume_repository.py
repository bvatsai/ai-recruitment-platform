from uuid import UUID
from sqlalchemy.orm import Session
from app.models.resume import Resume


class ResumeRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, resume: Resume):
        self.session.add(resume)
        self.session.commit()
        self.session.refresh(resume)
        return resume
    
    def update(self, resume: Resume):
        self.session.commit()
        self.session.refresh(resume)
        return resume
    
    def find_by_candidate_id(self, candidate_id: UUID):
        return (
        self.session.query(Resume)
        .filter(Resume.candidate_id == candidate_id)
        .first()
        )