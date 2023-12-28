from services import gpt_service
from flask import render_template
from App import app
from services import job_service

@app.route("/applicant-assessment")
def applicant_assessment(applicant:str, email:str, phone:str, links:list, major:str, skill_score:int, experience_score:int, questions:list):

    job_requirement = job_service.get_job()
    result_dict = gpt_service.get_scoring_and_question(job_requirement)
    
    applicant = result_dict['Applicant']
    email = result_dict['Email']
    phone = result_dict['Position']
    links = result_dict['Phone']    # list

    major = result_dict['Major']
    skill_score = result_dict['Skill matching score']
    experience_score = result_dict['Experience score']
    questions = result_dict['Interview questions']  # list
    
    return render_template("add-applicant.html", applicant, email, phone, links, major, skill_score, experience_score, questions)