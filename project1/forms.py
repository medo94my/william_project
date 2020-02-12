from flask_wtf import FlaskForm 
# from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from project1.Model import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max =20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max =10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max =20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class adminForm(FlaskForm):
    admin = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max =20)])
    submit = SubmitField('Login')

class CipherForm(FlaskForm):
    shift = StringField('Shift', validators=[DataRequired(), Length(min=0, max=2)])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Cipher IT!')

class VernamForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Cipher IT!')

class VernamdecryptForm(FlaskForm):
    encryptedmessage = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Cipher IT!')

class QuestionForm(FlaskForm):
    ques_id = HiddenField()
    answer = StringField('Answer', validators=[DataRequired()])
    answer2 = StringField('Answer', validators=[DataRequired()])
    answer3 = StringField('Answer', validators=[DataRequired()])
    answer4 = StringField('Answer', validators=[DataRequired()])
    answer5 = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField(' SUBMIT CORONAT!')

