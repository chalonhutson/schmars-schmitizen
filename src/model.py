from os import environ
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(99), unique = True, nullable = False)
    email = db.Column(db.String(99), unique = True, nullable = False)
    password = db.Column(db.String(299), nullable = False)

    users_ships = db.relationship("UserShip", backref = "user", lazy = True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


class Ship(db.Model):
    __tablename__ = "ships"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(99), unique = True, nullable = False)
    classification = db.Column(db.String(99), nullable = False)
    size = db.Column(db.String(99), nullable = False)
    speed = db.Column(db.String(99), nullable = False)
    crew_limit = db.Column(db.Integer, nullable = False)

    users_ships = db.relationship("UserShip", backref = "ship", lazy = True)

    def __init__(self, name, classification, size, speed, crew_limit):
        self.name = name
        self.classification = classification
        self.size = size
        self.speed = speed
        self.crew_limit = crew_limit

    def __repr__(self):
        return f"<Ship {self.name}>"


class UserShip(db.Model):
    __tablename__ = "users_ships"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False) 
    ship_id = db.Column(db.Integer, db.ForeignKey("ships.id"), nullable = False)
    
    def __init__(self, user_id, ship_id):
        self.user_id = user_id
        self.ship_id = ship_id


def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = environ["DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to Schmars Schmitizen database...")
