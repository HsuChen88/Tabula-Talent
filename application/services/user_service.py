# local library
from ..models.user import User
from ..app import db

# C
def create_user(fullname, email):
    new_user = User(fullname, email)
    db.session.add(new_user)
    db.session.commit()
    return new_user

# R
def get_user(id):
    user = db.session.get(User, id)
    return user

# U
def modify_user(id, fullname, email):
    user = db.session.get(User, id)
    user.fullname = fullname
    user.email = email
    db.session.merge(user)
    db.session.commit()
    return user

# D
def remove_user(id):
    user = db.session.get(User, id)
    db.session.delete(user)
    db.session.commit()
    return user
