# standard library
from typing import Any

# third party library
from sqlalchemy.orm import validates

# local library
from App import db
from models.jsonifiable import Jsonifiable

class Job(db.Model, Jsonifiable):
    __tablename__ = "job"

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    reponsibility = db.Column(db.JSON)
    requirement = db.Column(db.JSON)
    education = db.Column(db.JSON)

    db_job_applicant = db.relationship("Applicant", backref="job")

    def __init__(
        self, 
        position: str, 
        description: str, 
        reponsibility: str | dict[str, Any],
        requirement: str | dict[str, Any],
        education: str | dict[str, Any]
    ) -> None:
        self.position = position
        self.description = description
        self.reponsibility = reponsibility
        self.requirement = requirement
        self.education = education

    @validates("email")
    def validate_email(self, key, value):
        if "@" not in value:
            raise ValueError("invalid email pattern")
        return value

    def jsonify(self) -> dict[str, Any]:
        # 在 commit 後 __dict__ 會發生一些變動，因而只能手動列
        return {
            "id": self.id,
            "position": self.position,
            "description": self.description,
            "reponsibility": self.reponsibility,
            "requirement": self.requirement,
            "education": self.education,
        }
