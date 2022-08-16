from flask import Flask, render_template
from src.form import Login

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/", methods=["GET", "POST"])
def home():
    form = Login()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        print(username)
        print(password)
        print(remember_me)
    return render_template("login.html", title = "Login", form = form)
