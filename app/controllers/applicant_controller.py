# third party library
from flask import request, render_template, redirect, url_for
import json

# local library
from App import app
from services import applicant_service, job_service
from models.applicant import Applicant

################################################
################# add-applicant ################
################################################

@app.route("/add_applicant/<int:job_id>", methods=["GET"])
def add_applicant(job_id: int, applicant: Applicant = Applicant()):
    job = job_service.get_job(job_id)
    return render_template("add-applicant.html", job=job, applicant=applicant)

@app.route("/add_applicant/<int:job_id>/submit", methods=["POST"])
def add_applicant_submit(job_id: int):
    """
    Brief
    -----
    收到新增 applicant 表單，資料庫新增 applicant，頁面重導向至 "/add_applicant"
    """
    job = job_service.get_job(job_id)
    applicant_dict: dict = json.loads(request.form["submit-applicant"].replace("None", "null").replace("\'", "\""))
    applicant_dict.pop("id")
    print(applicant_dict)
    # 資料庫操作
    applicant_service.create_applicant(**applicant_dict)
    # return render_template("add-applicant.html", job=job, applicant=Applicant())

    applicants = Applicant.query.filter_by(job_id=job_id).all()
    return render_template('view-job.html', job=job, applicants=applicants)

