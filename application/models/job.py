# standard library
from typing import Any

# third party library
from sqlalchemy.orm import validates
 
# local library
from ..app import db
from .jsonifiable import Jsonifiable


# CREATE TABLE Job (
#     id SERIAL PRIMARY KEY,
#     position VARCHAR(50) NOT NULL, -- FOREIGN KEY
#     description TEXT,
#     responsibility JSON,
#     requirement JSON,
#     education JSON
# );

class Job(db.Model, Jsonifiable):

    __tablename__ = "job"

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    reponsibility = db.Column(db.JSON)
    requirement = db.Column(db.JSON)
    education = db.Column(db.JSON)

    def __init__(self, position, description, reponsibility, requirement, education) -> None:
        self.position = position
        self.description = description
        self.reponsibility = reponsibility
        self.requirement = requirement
        self.education = education

    def jsonify(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "position": self.position,
            "description": self.description,
            "reponsibility": self.reponsibility,
            "requirement": self.requirement,
            "education": self.education
        }