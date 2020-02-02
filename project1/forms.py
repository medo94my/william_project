from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from project1.Model import User


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max =10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max =20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max =20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class CipherForm(FlaskForm):
    shift = StringField('Shift', validators=[DataRequired(), Length(min=0, max=2)])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Cipher IT!')

