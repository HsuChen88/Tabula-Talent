from ..services import job_service


def test():
    print("Creating a job in Job Table...")
    position = "QA Software Engineer"
    description = "description - QA Software Engineer"
    reponsibility = """{"reponsibility": "QA Software Engineer"}"""
    requirement = """{"requirement": "QA Software Engineer"}"""
    education = """{"education": "QA Software Engineer"}"""
    job = job_service.create_job(
        position, description, reponsibility, requirement, education
    )
    print(job.jsonify())

    print("Try to get the job we just added...")
    returned_job = job_service.get_job(job.id)
    print(returned_job.jsonify())

    print("Try to modify the job we just added...")
    returned_job = job_service.modify_job(
        job.position, description="modified description - QA Software Engineer"
    )
    print(returned_job.jsonify())

    print("Try to remove the job we just added...")
    job_service.remove_job(job.id)
    if not job_service.get_job(job.id):
        print("Remove successfully.")
    else:
        print("Remove process has failed.")