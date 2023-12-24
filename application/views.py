# third party library
from flask import request, render_template

# local library
from .services import job_service

def views(app):

    # 顯示表單
    @app.route("/")
    def index():
        return render_template("add-job.html")

    # client 發送 POST 請求的處理路由
    @app.route("/submit", methods=["POST"])
    def submit_job_form():
        if request.method == "POST":
            position = request.form["position"]
            description = request.form["description"]
            responsibility = request.form["responsibility"]
            requirement = request.form["requirement"]
            educational_qualification = request.form["educational-qualification"]
            
            new_job = job_service.create_job(position, description, responsibility, requirement, educational_qualification)
            
            # 回傳回應 str 給用戶
            return str(new_job.jsonify())