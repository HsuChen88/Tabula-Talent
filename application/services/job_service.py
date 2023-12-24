# local library
from ..models.job import Job
from ..app import db

# C
def create_job(position, description, reponsibility, requirement, education):
    new_job = Job(position, description, reponsibility, requirement, education)
    db.session.add(new_job)
    db.session.commit()
    return new_job

# R
def get_job(id):
    job = db.session.get(Job, id)
    return job

# U (不可更改 position 名稱)
def modify_job(position, **kwargs):
    job: Job = Job.query.filter_by(position=position).first()
    for key, val in kwargs.items():
        if key == "position":
            raise AttributeError("You cannot edit position column.")
        elif key in vars(job).keys() and val is not None:
            setattr(job, key, val)
    db.session.merge(job)
    db.session.commit()
    return job

# D
def remove_job(id):
    job = db.session.get(Job, id)
    db.session.delete(job)
    db.session.commit()
    return job
