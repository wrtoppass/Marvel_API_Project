from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class SigninForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    body = StringField('body', validators=[DataRequired()])
    submit = SubmitField('Publish')

class UserSearchForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    submit = SubmitField('Search')