# standard library
from http import HTTPStatus

# third party library
from flask import Response, request, render_template

# local library
from App import app, db
from models.job import Job
from services import job_service

@app.route("/")
def index_template():
    return "<h1>Hello Flask!</h1>"

@app.route("/add_job")
def add_job_template():
    return render_template("add-job.html")

@app.route("/job", methods=["GET"])
def get_job():
    try:
        position = request.args.get("position")
        job = job_service.get_job(position)
        return str(job.jsonify())
    except AttributeError:
        return {"message": "no elements found"}, HTTPStatus.BAD_REQUEST
    except:
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@app.route("/job", methods=["POST"])
def create_job():
    try:
        position = request.form["position"]
        description = request.form["description"]
        responsibility = request.form["responsibility"]
        requirement = request.form["requirement"]
        educational_qualification = request.form["educational-qualification"]
        new_job: Job = job_service.create_job(position, description, responsibility, requirement, educational_qualification)
        return str(new_job.jsonify()), HTTPStatus.CREATED
    except KeyError as err:
        return {"message": "key required not found", "key": err.args[0]}, HTTPStatus.BAD_REQUEST
    except ValueError as err:
        return {"message": err.args[0]}, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as err:
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@app.route("/get_all")
def get_all_jobs():
    all_jobs = [str(job.jsonify()) for job in Job.query.all()]
    return "<br>".join(all_jobs)

@app.route("/remove_all")
def remove_all_jobs():
    Job.query.delete()
    db.session.commit()
    return "Remove successfully."