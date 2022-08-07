from flask import Flask
from forms import Login

app = Flask(__name__)

@app.route("/")
def home():
    form = Login()

    return "Welcome to Schmars Schmitizen!"
