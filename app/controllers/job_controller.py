# standard library
from http import HTTPStatus

# third party library
from flask import Response, request, render_template, redirect, url_for

# local library
from App import app, db
from services import job_service, applicant_service
from models.job import Job
from models.applicant import Applicant

################################################
##################### home #####################
################################################

@app.route("/", methods=["GET"])
def home():
    job_list = Job.query.all()
    return render_template("home.html",
                           job_list=job_list)

################################################
################### view-job ###################
################################################

@app.route("/view_job/<int:id>", methods=["GET"])
def view_job(id: int):
    job = job_service.get_job(id)
    applicants = Applicant.query.filter_by(job_id=id).all()
    return render_template("view-job.html", 
                           job=job, applicants=applicants)

################################################
#################### add-job ###################
################################################

@app.route("/add_job", methods=["GET"])
def add_job():
    return render_template("add-job.html")

@app.route("/add_job/submit", methods=["POST"])
def add_job_submit():
    """
    Brief
    -----
    收到新增 job 表單，資料庫新增 job，頁面重導向至 "/add_job"
    """
    position = request.form["position"]
    description = request.form["description"]
    responsibility = request.form["responsibility"]
    requirement = request.form["requirement"]
    education = request.form["education"]

    # 資料庫操作
    job_service.create_job(position, description, responsibility, requirement, education)

    return redirect(url_for("home"))














# @app.route("/job", methods=["GET"])
# def get_job():
#     try:
#         position = request.args.get("position")
#         job = job_service.get_job(position)
#         return str(job.jsonify())
#     except AttributeError:
#         return {"message": "no elements found"}, HTTPStatus.BAD_REQUEST
#     except:
#         return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

# @app.route("/job", methods=["POST"])
# def create_job():
#     try:
#         position = request.form["position"]
#         description = request.form["description"]
#         responsibility = request.form["responsibility"]
#         requirement = request.form["requirement"]
#         educational_qualification = request.form["educational-qualification"]
#         new_job: Job = job_service.create_job(position, description, responsibility, requirement, educational_qualification)
#         return str(new_job.jsonify()), HTTPStatus.CREATED
#     except KeyError as err:
#         return {"message": "key required not found", "key": err.args[0]}, HTTPStatus.BAD_REQUEST
#     except ValueError as err:
#         return {"message": err.args[0]}, HTTPStatus.UNPROCESSABLE_ENTITY
#     except Exception as err:
#         return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

# @app.route("/get_all")
# def get_all_jobs():
#     all_jobs = [str(job.jsonify()) for job in Job.query.all()]
#     return "<br>".join(all_jobs)

# @app.route("/remove_all")
# def remove_all_jobs():
#     Job.query.delete()
#     db.session.commit()
#     return "Remove successfully."