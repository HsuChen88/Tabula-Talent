# standard libraary
import os

# third party library
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)

# 如果資料庫沒有建置表格的話，全部建置
with app.app_context():
    db.create_all()

# local library
from .views import views

views(app)