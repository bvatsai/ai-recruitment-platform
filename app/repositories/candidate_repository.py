from app.candidate.candidate import Candidate   #jumps to the file app/candidate/candidate.py and imports the Candidate class defined in that file. This class represents a candidate entity in the system, containing attributes such as candidate_id, profile, and resume. It serves as a data model for candidates and is used throughout the application to manage candidate-related operations.

class CandidateRepository:

    def __init__(self):
        self._candidates: list[Candidate] = []

    def save(self, candidate: Candidate) -> None:
        self._candidates.append(candidate)

    def get_all(self) -> list[Candidate]:
        return self._candidates