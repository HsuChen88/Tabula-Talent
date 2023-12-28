# third party library
from flask import request, render_template, redirect, url_for

# local library
from App import app
from services import applicant_service

################################################
################# add-applicant ################
################################################

@app.route("/add_applicant", methods=["GET"])
def add_applicant():
    return render_template("add-applicant.html")

@app.route("/add_applicant/submit", methods=["POST"])
def add_applicant_submit():
    """
    Brief
    -----
    收到新增 applicant 表單，資料庫新增 applicant，頁面重導向至 "/add_applicant"
    """
    position = request.form["position"]
    description = request.form["description"]
    responsility = request.form["responsility"]
    education = request.form["education"]
    
    # 資料庫操作...
    print(f"{position}, {description}, {responsility}, {education}")

    return redirect(url_for("add_applicant"))