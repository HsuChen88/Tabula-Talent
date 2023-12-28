# # standard library
# from pprint import pprint

# # local library
# from services import job_service


# def test(remove: bool = True):
    
#     print("******************************************************")
    
#     print("Creat a job in Job Table...")
#     position = "QA Software Engineer"
#     description = "description - QA Software Engineer"
#     responsibility = """{"responsibility": "QA Software Engineer"}"""
#     requirement = """{"requirement": "QA Software Engineer"}"""
#     education = """{"education": "QA Software Engineer"}"""
#     job = job_service.create_job(
#         position, description, responsibility, requirement, education
#     )
#     pprint(job.jsonify())

#     print("******************************************************")
    
#     print("Try to get the job we just added...")
#     returned_job = job_service.get_job(job.position)
#     pprint(returned_job.jsonify())

#     print("******************************************************")

#     print("Try to modify the description of job we just added...")
#     job_service.modify_job(
#         job.position, description="#modified"
#     )
#     returned_job = job_service.get_job(job.position)
#     pprint(returned_job.jsonify())

#     print("******************************************************")
#     if remove:
#         print("Try to remove the job we just added...")
#         job_service.remove_job(job.position)
#         if not job_service.get_job(job.position):
#             print("Remove successfully.")
#         else:
#             print("Remove process has failed.")
#     else:
#         print("Remove cancelld.")
#     print("******************************************************")