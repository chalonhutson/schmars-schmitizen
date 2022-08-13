from flask import Flask, render_template
from src.form import Login

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/")
def home():
    form = Login()
    username = form.username.data
    password = form.password.data
    remember_me = form.remember_me.data
    return render_template("login.html", title = "Login", form = form)
