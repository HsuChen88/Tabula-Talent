# standard libraary
import os

# third party library
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
# from openai import OpenAI, api_key

app = Flask(__name__)
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)

# client_gpt = OpenAI()
# api_key = os.getenv("OPENAI_API_KEY")

with app.app_context():
    db.create_all() # 如果資料庫沒有建置表格的話，全部建置

from controllers import *
