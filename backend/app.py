import json

from flask import Flask, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
import os
import sqlite3
import math

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.permanent_session_lifetime = timedelta(minutes=10)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

def square_root(x):
    return math.sqrt(x)

def square(x):
    return x*x


def is_someone_logged_in(session):
    if "name" in session:
        return True
    else:
        return False

response = {"message" : "nothing", "success" : 0}

@app.route('/')
def index():
    if is_someone_logged_in(session):
        #message: someone already logged in
        response["message"] = session["name"] + " already logged in"
        response["success"] = 0
        return json.dumps(response)
    else:
        return "Hello World!"

@app.route("/login", methods=["POST"])
def login():
    if is_someone_logged_in(session):
        response["message"] = session["name"] + " already logged in"
        response["success"] = 0
        return json.dumps(response)

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        #if(name in database and password verified) then session["name"] = name (indication of logged user)

        found_user = users.query.filter_by(name=name).first()
        if found_user:
            if sha256_crypt.verify(password, found_user.password):
                session.permanent = True
                session["name"] = name
                response["message"] = session["name"] + " logged in"
                response["success"] = 1
                return json.dumps(response)
            else:
                response["message"] = "incorrect password for " + session["name"]
                response["success"] = 0
                return json.dumps(response)
        else:
            response["message"] = session["name"] + " not in database"
            response["success"] = 0
            return json.dumps(response)

@app.route("/logout")
def logout():
    if is_someone_logged_in(session):
        name = session["name"]
        session.clear()
        response["message"] = session["name"] + " logged out"
        response["success"] = 1
        return json.dumps(response)
    else:
        response["message"] = "nobody's logged in"
        response["success"] = 0
        return json.dumps(response)

@app.route("/signup", methods=["POST"])
def signup():

    if is_someone_logged_in(session):
        response["message"] = session["name"] + " already logged in"
        response["success"] = 0
        return json.dumps(response)

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        #if name is not in database already, add new record=(name, password.encrypt()) to it
        #if it is, then message:"user already exists", success:"False"

        if users.query.filter_by(name=name).first():
            response["message"] = session["name"] + " already in database"
            response["success"] = 0
            return json.dumps(response)
        else:
            user = users(name, sha256_crypt.encrypt(password))
            db.session.add(user)
            db.commit()
            response["message"] = session["name"] + " added"
            response["success"] = 1
            return json.dumps(response)

#
@app.route("/search", methods=["POST"])
def search():
    client_coordinate_x = float(request.form["client_coordinate_x"])
    client_coordinate_y = float(request.form["client_coordinate_y"])
    radius = float(request.form["radius"])
    activities = json.loads(request.form["activities"]) #returns some kind of json list, has to be converted into python list

    print(client_coordinate_x)
    print(client_coordinate_y)
    print(radius)
    print(activities)

    places = []

    #DATABASE FETCH(SELECT): load into variable places (what data structure is returned from the fetch)

    params = [client_coordinate_x, client_coordinate_y, radius]
    db = sqlite3.connect("McKinsey.db")
    db.create_function("square_root",1,square_root)
    db.create_function("square",1,square)
    query = "select p.*, 111*(square_root(square(p.coordinate_x - ?)+ square(p.coordinate_y - ?))) distance  from Places p where distance < ? order by distance"
    c = db.cursor()
    c.execute(query, params)
    places = c.fetchall()
    c.close()

    json_to_be_returned = json.dumps(places,indent=2)

    return json_to_be_returned


if __name__ == '__main__':
    app.run(debug=True);