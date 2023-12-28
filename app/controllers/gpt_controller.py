# from models.gpt_message import GptMessage

# from App import client_gpt, app

# def get_resume_text():
    
#     resume_text = ""
    
#     with open("../resource/recognized.txt", "r", encoding="utf-8") as file:
#         for line in file:
#             resume_text += line
    
#     return resume_text

# @app.route("/applicant-assessment")
# def get_applicant_scoring(job_requirement: str) -> dict:

#     resume_text = get_resume_text()
#     response = client_gpt.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": """You are a human resources manager. Input are resume (text) and the job requirements (JSON). You need to review the resume to see if the position the applicant is applying for is same as the position to be recruited, and whether the applicant meets the skills, experience, etc. required for the position. Aspect scores (1-10), and then based on the information in the resume, questions that can be asked in the interview are generated. Output the results in json format, for example: {"Position": "(position being applied)", "Major": "(highest degree major)", "Skill matching score": (1-10), "Experience score" :(1-10), "Interview questions":"[(question1), (question2), ...]"}"""},
#             {"role": "user", "content": f"Job Requirement:\n{job_requirement}\nResume text:\n{resume_text}"}
#         ],
#         temperature=1,
#         max_tokens=2000,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     response_text = response.choices[0].message.content
#     message = GptMessage(response_text)
#     message_dict = message.parse_json()
    
#     return message_dict
