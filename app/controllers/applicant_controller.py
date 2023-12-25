# third party library
from flask import request, render_template

# local library
from App import app
from services import applicant_service

# applicant 表單處理路由
@app.route("/submit/applicant", methods=["POST"])
def submit_applicant_form():
    if request.method == "POST":
        return NotImplemented