# # local library
# from services import applicant_service, job_service


# def test():
    
#     print("******************************************************")

#     print("Creating a applicant in Applicant Table...")
#     name = "RogelioKG"
#     phone = "0912345678"
#     email = "123456@gmail.com"
#     link = ""
#     major = "Computer Science and Information Engineering"
#     questions = """{'1': 'Q1', '2': 'Q2', '3': 'Q3', '4': 'Q4', '5': 'Q5'}"""
#     skill_score = 5
#     experience_score = 8
#     interview_score = 9
#     position = "QA Software Engineer"
#     job_id = job_service.get_job(position).id
#     applicant = applicant_service.create_applicant(
#         name,
#         phone,
#         email,
#         link,
#         major,
#         questions,
#         skill_score,
#         experience_score,
#         interview_score,
#         job_id,
#     )
#     print(applicant.jsonify())
    
#     print("******************************************************")

#     print("Try to get the applicant we just added...")
#     returned_applicant = applicant_service.get_applicant(applicant.id)
#     print(returned_applicant.jsonify())

#     print("******************************************************")

#     print("Try to modify the applicant we just added...")
#     returned_applicant = applicant_service.modify_applicant(
#         applicant.id, experience_score=7
#     )
#     print(returned_applicant.jsonify())
    
#     print("******************************************************")

#     print("Try to remove the applicant we just added...")
#     applicant_service.remove_applicant(applicant.id)
#     if not applicant_service.get_applicant(applicant.id):
#         print("Remove successfully.")
#     else:
#         print("Remove process has failed.")
        
#     print("******************************************************")
