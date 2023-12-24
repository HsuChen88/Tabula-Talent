from models.User import User
from App import db

def get_user(id):
    user = db.session.get(User, id)
    return user

def create_user(fullname, email):
    new_user = User(fullname, email)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def modify_user(id, fullname, email):
    user = db.session.get(User, id)
    user.fullname = fullname
    user.email = email
    db.session.merge(user)
    db.session.commit()
    return user

def remove_user(id):
    user = db.session.get(User, id)
    db.session.delete(user)
    db.session.commit()
    return user
