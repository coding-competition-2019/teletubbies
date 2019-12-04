import json

from flask import Flask, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.permanent_session_lifetime = timedelta(minutes=10)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, password):
        self.name = name
        self.password = password


def is_someone_logged_in(session):
    if "name" in session:
        return True
    else:
        return False


@app.route('/')
def index():
    if is_someone_logged_in(session):
        #message: someone already logged in
        return session["name"] + " already logged in"
    else:
        return "Hello World!"

@app.route("/login", methods=["POST"])
def login():
    if is_someone_logged_in(session):
        #message: someone already logged in
        return session["name"] + " already logged in"

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        #if(name in database and password verified) then session["name"] = name (indication of logged user)

        found_user = users.query.filter_by(name=name).first()
        if found_user:
            if sha256_crypt.verify(password, found_user.password):
                session.permanent = True
                session["name"] = name
                #EOK
            else:
                #Incorrect password
                return "incorrect password"
        else:
            #name not in database
            return "name not in database"

@app.route("/logout")
def logout():
    if is_someone_logged_in(session):
        name = session["name"]
        session.clear()
        return name + " logged out"
    else:
        #message: Nobody's logged in
        return "nobody's logged in"

@app.route("/signup", methods=["POST"])
def signup():

    if is_someone_logged_in(session):
        #message: someone already logged in
        return session["name"] + " already logged in"

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        #if name is not in database already, add new record=(name, password.encrypt()) to it
        #if it is, then message:"user already exists", success:"False"

        if users.query.filter_by(name=name).first():
            #already in database
            return "already in database"
        else:
            user = users(name, sha256_crypt.encrypt(password))
            db.session.add(user)
            db.commit()
            #EOK
            return "user added"

#
@app.route("/search", methods=["POST"])
def search():
    coordinate_x = int(request.form["coordinate_x"])
    coordinate_y = int(request.form["coordinate_y"])
    radius = int(request.form["radius"])
    activities = request.form["activities"] #returns some kind of json list, has to be converted into python list

    #DATABASE FETCH(SELECT): load into variable places (what data structure is returned from the fetch)

    places = [] #list of dictionaries, i guess

    json_to_be_returned = json.dump(places, indent=2)

    return json_to_be_returned


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True);