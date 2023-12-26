# standard library
from typing import Any

# local library
from models.job import Job
from App import db


# C
def create_job(
    position: str,
    description: str,
    reponsibility: str | dict[str, Any],
    requirement: str | dict[str, Any],
    education: str | dict[str, Any],
) -> Job:
    new_job = Job(position, description, reponsibility, requirement, education)
    db.session.add(new_job)
    db.session.commit()
    return new_job


# R
def get_job(position: str) -> Job | None:
    job = Job.query.filter_by(position=position).first()
    return job


# U (不可更改 position)
def modify_job(position: str, **kwargs) -> Job | None:
    job = Job.query.filter_by(position=position).first()
    for key, val in kwargs.items():
        if key == "position":
            raise AttributeError("You cannot edit position column.")
        elif key in vars(job).keys() and val is not None:
            setattr(job, key, val)
    db.session.merge(job)
    db.session.commit()
    return job

# D
def remove_job(position: str) -> Job | None:
    job = Job.query.filter_by(position=position).first()
    db.session.delete(job)
    db.session.commit()
    return job
