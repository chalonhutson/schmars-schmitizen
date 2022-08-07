from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, PasswordField, SubmitField


class Login(FlaskForm):
    username = StringField("username", validators = [DataRequired(), Length(min=4, max=99))
    password = PasswordField("password", validators = [DataRequired(), Length(min=4, max=99))
    submit = SubmitField("submit")
