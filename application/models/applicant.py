# standard library
from typing import Any

# third party library
from sqlalchemy.orm import validates

# local library
from ..app import db
from .jsonifiable import Jsonifiable


# CREATE TABLE Applicant (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(30) NOT NULL, 
#     phone VARCHAR(15),
#     email TEXT,
#     link JSON,
#     major JSON,
#     questions JSON
#     skill_score INT,
#     experience_score INT,
#     interview_score INT,
#     position VARCHAR(50) NOT NULL -- FOREIGN KEY
# );

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
    position = db.Column(db.String(50), nullable=False)

    def __init__(
        self,
        name,
        phone,
        email,
        link,
        major,
        questions,
        skill_score,
        experience_score,
        interview_score,
        position
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
        self.position = position

    def jsonify(self) -> dict[str, Any]:
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
            "position": self.position
        }
