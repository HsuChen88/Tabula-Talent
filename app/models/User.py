from sqlalchemy.orm import validates

from App import db
from models.Jsonifiable import Jsonifiable

class User(db.Model, Jsonifiable):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    @validates("email")
    def validate_email(self, key, value):
        if "@" not in value:
            raise ValueError("invalid email pattern")
        return value

    def __init__(self, fullname, email):
        self.fullname  = fullname
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.fullname, self.email)

    def jsonify(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "email": self.email
        }
