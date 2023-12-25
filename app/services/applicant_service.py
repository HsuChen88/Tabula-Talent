# standard library
from typing import Any

# local library
from models.applicant import Applicant
from App import db


# C
def create_applicant(
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
):
    new_applicant = Applicant(
        name,
        phone,
        email,
        link,
        major,
        questions,
        skill_score,
        experience_score,
        interview_score,
        job_id,
    )
    db.session.add(new_applicant)
    db.session.commit()
    return new_applicant

# R
def get_applicant(id: int):
    applicant = db.session.get(Applicant, id)
    return applicant


# U
def modify_applicant(id: int, **kwargs):
    applicant = db.session.get(Applicant, id)
    for key, val in kwargs.items():
        if key in vars(applicant).keys() and val is not None:
            setattr(applicant, key, val)
    db.session.merge(applicant)
    db.session.commit()
    return applicant

# D
def remove_applicant(id: int):
    applicant = db.session.get(Applicant, id)
    db.session.delete(applicant)
    db.session.commit()
    return applicant
