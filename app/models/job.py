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
    responsibility = db.Column(db.Text)
    requirement = db.Column(db.Text)
    education = db.Column(db.Text)
    db_job_applicant = db.relationship("Applicant", backref="job")

    def __init__(
        self, 
        position: str, 
        description: str, 
        responsibility: str,
        requirement: str,
        education: str
    ) -> None:
        self.position = position
        self.description = description
        self.responsibility = responsibility
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
            "responsibility": self.responsibility,
            "requirement": self.requirement,
            "education": self.education,
        }
