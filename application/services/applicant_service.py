# local library
from ..models.applicant import Applicant
from ..app import db


# C
def create_applicant(
    name,
    phone,
    email,
    link,
    major,
    questions,
    skill_score,
    experience_score,
    interview_score,
    position,
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
        position,
    )
    db.session.add(new_applicant)
    db.session.commit()
    return new_applicant


# R
def get_applicant(id):
    applicant = db.session.get(Applicant, id)
    return applicant


# U
def modify_applicant(id, **kwargs):
    applicant = db.session.get(Applicant, id)
    for key, val in kwargs.items():
        if key in vars(applicant).keys() and val is not None:
            setattr(applicant, key, val)
    db.session.merge(applicant)
    db.session.commit()
    return applicant

# D
def remove_applicant(id):
    applicant = db.session.get(Applicant, id)
    db.session.delete(applicant)
    db.session.commit()
    return applicant
