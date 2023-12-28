# third party library
from flask import request, render_template, redirect, url_for

# local library
from App import app
from services import applicant_service
from services import job_service

################################################
################# add-applicant ################
################################################

@app.route("/add_applicant/<int:id>")
def add_applicant(id: int, name: str='', email: str='', phone: str='', major: str= '', skill_score: str="", experience_score: str=""):
    job = job_service.get_job(id)
    return render_template("add-applicant.html", job=job, name=name, email=email, phone=phone, major=major, skill_score=skill_score, experience_score=experience_score)

@app.route("/add_applicant/<int:id>/submit", methods=["POST"])
def add_applicant_submit(id: int):
    """
    Brief
    -----
    收到新增 applicant 表單，資料庫新增 applicant，頁面重導向至 "/add_applicant"
    """
    job = job_service.get_job(id)

    if request.methods == "POST":
        
        username = request.form.get('username')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        # 資料庫操作...
        
        return redirect(url_for("add_applicant"), job=job, name='', email='', phone='', major= '', skill_score="", experience_score="")
    else:
        return 