from services import resume_service, gpt_service
from flask import render_template

from App import app

@app.route("/resume-recognition", methods = ['POST'])
def resume_recognition():
    
    resume_text = resume_service.recognize_resume_image("eng_resume1.jpg")
    
    return "<article>"+resume_text+"</article>"
    # return render_template('add-applicant.html')