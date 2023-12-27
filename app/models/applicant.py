# standard library
from typing import Any

# local library
from App import db
from models.jsonifiable import Jsonifiable

class Applicant(db.Model, Jsonifiable):
    __tablename__ = "applicant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(15))
    email = db.Column(db.Text)
    link = db.Column(db.JSON)
    major = db.Column(db.String(50))
    questions = db.Column(db.JSON)
    skill_score = db.Column(db.Integer)
    experience_score = db.Column(db.Integer)
    interview_score = db.Column(db.Integer)
    job_id = db.Column(db.Integer, db.ForeignKey("job.id"), nullable=False)

    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
        link: str | dict[str, Any],
        major: str,
        questions: str | dict[str, Any],
        skill_score: int,
        experience_score: int,
        interview_score: int,
        job_id: int
    ) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.link = link
        self.major = major
        self.questions = questions
        self.skill_score = skill_score
        self.experience_score = experience_score
        self.interview_score = interview_score
        self.job_id = job_id

    def jsonify(self) -> dict[str, Any]:
        # 在 commit 後 __dict__ 會發生一些變動，因而只能手動列
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "link": self.link,
            "questions": self.questions,
            "skill_score": self.skill_score,
            "experience_score": self.experience_score,
            "interview_score": self.interview_score,
            "job_id": self.job_id
        }
