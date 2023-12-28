# standard library
from http import HTTPStatus

# third party library
from flask import Response, request, render_template, redirect, url_for

# local library
from App import app, db
from services import job_service
from models.job import Job


################################################
############# pre-interview-report #############
################################################

@app.route("/pre_interview_report", methods=["GET"])
def pre_interview_report():
    return render_template("pre-interview-report.html")

################################################
################# final-result #################
################################################

@app.route("/final_result", methods=["GET"])
def final_result():
    return "<h1>Under construction</h1>"