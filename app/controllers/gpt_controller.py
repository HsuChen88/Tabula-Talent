# standard library
import os

# third party library
from flask import request, render_template, redirect, url_for

# local library
from App import app
from services import job_service, gpt_service, resume_service
from models.applicant import Applicant

@app.route("/applicant_assessment/<int:job_id>", methods=["POST"])
def applicant_assessment(job_id: int):
    if request.method == "POST":
        job = job_service.get_job(job_id)
        job_requirement = str(job.jsonify())

        # 無法使用 image
        # resume_image = request.files["resume"]
        # resume_image_path = "." + os.getcwd() + "/resource/" + resume_image.filename
        # resume_image.save(resume_image_path)
        # resume_text = resume_service.recognize_resume_image(resume_image_path)

        with open("." + os.getcwd() + "/resource/demo_resume2.txt", "r", encoding="utf-8") as file:
            resume_text = file.read()
        gpt_message = gpt_service.get_gpt_assessment(job_requirement, resume_text)

        assessment = gpt_message.parse_json()

        # applicant = Applicant("Say my name", 
        #                     "phone", 
        #                     "email",
        #                     {"GitHub": "link here", "LinkedIn": "link here"}, 
        #                     "major",
        #                     ["questions"],
        #                     0, 
        #                     0, 
        #                     0,
        #                     job.id)

        applicant = Applicant()
        applicant.name = assessment["Applicant"]
        applicant.phone = assessment["Phone"]
        applicant.email = assessment["Email"]
        applicant.link = assessment["Link"]
        applicant.major = assessment["Major"]
        applicant.questions = assessment["Interview Questions"]  # list
        applicant.skill_score = assessment["Skill Match Score"]
        applicant.experience_score = assessment["Experience Score"]
        applicant.job_id = job_id
        
    return render_template("add-applicant.html", job=job, applicant=applicant)