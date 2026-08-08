from uuid import UUID

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.database import get_session
from app.repositories.resume_repository import ResumeRepository
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.post("/upload")
def upload_resume(
    candidate_id: UUID,
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    repository = ResumeRepository(session)
    service = ResumeService(repository)

    return service.upload_resume(candidate_id, file)