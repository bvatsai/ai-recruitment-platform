from app.repositories.resume_repository import ResumeRepository
from app.ai.parsers.pdf_parser import PdfParser
from uuid import UUID
import shutil
from pathlib import Path
from uuid import UUID, uuid4
from fastapi import HTTPException, UploadFile
from app.models.resume import Resume

class ResumeService:

    def __init__(self, repository: ResumeRepository):
        self.repository = repository

    def upload_resume(
    self,
    candidate_id: UUID,
    file: UploadFile
    ):
        storage_path = Path("storage/resumes")
        storage_path.mkdir(parents=True, exist_ok=True)
        file_name = f"{uuid4()}.pdf"
        file_path = storage_path / file_name
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        existing_resume = self.repository.find_by_candidate_id(candidate_id)
        if existing_resume:
            old_file = Path(existing_resume.file_path)

            if old_file.exists():
                old_file.unlink()

            parser = PdfParser()
            text = parser.extract_text(str(file_path))

            existing_resume.file_path = str(file_path)
            existing_resume.extracted_text = text

            resume = self.repository.update(existing_resume)
        else:
            parser = PdfParser()
            text = parser.extract_text(str(file_path))

            resume = Resume(
                candidate_id=candidate_id,
                file_path=str(file_path),
                extracted_text=text
            )

            resume = self.repository.save(resume)

        return {
        "resume_id": resume.resume_id,
        "file_path": resume.file_path
        }