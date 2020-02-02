from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from project1 import  login_manager , db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10), unique = True,  nullable = False)
    email = db.Column(db.String(120), unique = True,  nullable = False)
    password = db.Column(db.String(60), nullable = False)



