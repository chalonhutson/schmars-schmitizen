from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class Login(FlaskForm):
    username = StringField("username", validators = [DataRequired(), Length(min=4, max=99)])
    password = PasswordField("password", validators = [DataRequired(), Length(min=4, max=99)])
    remember_me = BooleanField("remember me")
    submit = SubmitField("submit")
