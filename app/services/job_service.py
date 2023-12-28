# standard library
from typing import Any

# local library
from models.job import Job
from App import db


# C
def create_job(
    position: str,
    description: str,
    responsibility: str,
    requirement: str,
    education: str,
) -> Job:
    new_job = Job(position, description, responsibility, requirement, education)
    db.session.add(new_job)
    db.session.commit()
    return new_job


# R
def get_job(id: int) -> Job | None:
    job = db.session.get(Job, id)
    return job


# U (不可更改 position)
def modify_job(id: int, **kwargs) -> Job | None:
    job = db.session.get(Job, id)
    for key, val in kwargs.items():
        if key == "position":
            raise AttributeError("You cannot edit position column.")
        elif key in vars(job).keys() and val is not None:
            setattr(job, key, val)
    db.session.merge(job)
    db.session.commit()
    return job

# D
def remove_job(id: int) -> Job | None:
    job = db.session.get(Job, id)
    db.session.delete(job)
    db.session.commit()
    return job
