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


class Question(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key = True)
    Question = db.Column(db.String(10),   nullable = False)
    Submitted_by = db.Column(db.String(60), nullable = False)

class Answers(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key = True)
    Answers1 = db.Column(db.String(10),   nullable = False)
    Answers2 = db.Column(db.String(10),   nullable = False)
    Answer3 = db.Column(db.String(10),   nullable = False)
    Answers4 = db.Column(db.String(10),   nullable = False)
    Answers5 = db.Column(db.String(10),   nullable = False)
    Submitted_by = db.Column(db.Integer, nullable = False)



