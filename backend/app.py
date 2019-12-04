import json

from flask import Flask, request, session
from datetime import timedelta

from flask_cors import CORS, cross_origin
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
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
def square_root(x):
    return math.sqrt(x)

def square(x):
    return x*x

def distance(lat1, lon1, lat2, lon2):
    r = 6378.0

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1

    a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    dist = r * c

    return dist


def is_someone_logged_in(session):
    if "name" in session:
        return True
    else:
        return False

response = {"message" : "nothing", "success" : 0}

@app.route('/')
@cross_origin(origin='localhost',headers=['Content- Type'])
def index():
    if is_someone_logged_in(session):
        #message: someone already logged in
        response["message"] = session["name"] + " already logged in"
        response["success"] = 0
        return json.dumps(response)
    else:
        response["message"] = "nobody's logged in"
        response["success"] = 1
        return json.dumps(response)

@app.route("/login", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content- Type'])
def login():
    if is_someone_logged_in(session):
        response["message"] = session["name"] + " already logged in"
        response["success"] = 0
        return json.dumps(response)

    if request.method == "POST":
        request_data = json.dumps(request.data)
        name = str(request_data["name"])
        password = str(request_data["password"])

        #if(name in database and password verified) then session["name"] = name (indication of logged user)
        get_query = "select password from Users where username = ?"
        db = sqlite3.connect("McKinsey.db")
        c = db.cursor()
        c.execute(get_query, [name])
        found_pass = c.fetchall()
        print(found_pass)
        c.close()
        if found_pass:
            if sha256_crypt.verify(password, found_pass[0][0]):
                session.permanent = True
                session["name"] = name
                response["message"] = session["name"] + " logged in"
                response["success"] = 0
                return json.dumps(response)
            else:
                response["message"] = "incorrect password for " + session["name"]
                response["success"] = 1
                return json.dumps(response)
        else:
            response["message"] = session["name"] + " not in database"
            response["success"] = 1
            return json.dumps(response)

@app.route("/logout")
@cross_origin(origin='localhost',headers=['Content- Type'])
def logout():
    if is_someone_logged_in(session):
        name = session["name"]
        session.clear()
        response["message"] = session["name"] + " logged out"
        response["success"] = 0
        return json.dumps(response)
    else:
        response["message"] = "nobody's logged in"
        response["success"] = 1
        return json.dumps(response)

@app.route("/signup", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content- Type'])
def signup():

    if is_someone_logged_in(session):
        response["message"] = session["name"] + " already logged in"
        response["success"] = 1
        return json.dumps(response)

    if request.method == "POST":
        request_data = json.dumps(request.data)
        name = str(request_data["name"])
        password = str(request_data["password"])
        email = str(request_data["email"])
        #if name is not in database already, add new record=(name, password.encrypt()) to it
        #if it is, then message:"user already exists", success:"False"


        column = [name, email, sha256_crypt.encrypt(password)]
        db = sqlite3.connect("McKinsey.db")
        c = db.cursor()

        get_query = "select username from Users u where u.username = ?"
        c.execute(get_query, [name])
        exists = c.fetchall()
        print(exists)
        c.close()


        if len(exists)>0:
            response["message"] = name + " already in database"
            response["success"] = 1
            return json.dumps(response)
        else:

            query = "insert into Users(username, email, password) values (?, ?, ?)"
            c = db.cursor()
            c.execute(query, column)
            db.commit()
            c.close()
            response["message"] = name + " added"
            response["success"] = 0
            return json.dumps(response)

#
@app.route("/search", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content- Type'])
def search():
    if is_someone_logged_in(session) or True:
        json_data = json.loads(request.data)
        client_coordinate_x = float(json_data["client_coordinate_x"])
        client_coordinate_y = float(json_data["client_coordinate_y"])
        radius = float(json_data["radius"])
        activities = json_data["activities"]  # returns some kind of json list, has to be converted into python list

        activities_data = activities.split(",")
        print(activities_data)
        places = []

        # DATABASE FETCH(SELECT): load into variable places (what data structure is returned from the fetch)

        params = [client_coordinate_x, client_coordinate_y, radius]
        db = sqlite3.connect("McKinsey.db")
        db.create_function("square_root", 1, square_root)
        db.create_function("square", 1, square)
        db.create_function("get_distance", 4, distance)
        query = "select p.*, get_distance(p.coordinate_x, p.coordinate_y, ?, ?) distance  from Places p where distance < ? order by distance"
        c = db.cursor()
        c.execute(query, params)
        places = c.fetchall()
        activities_set = set(activities_data)
        return_places = []

        if(len(activities_set) < 1):
            return_places = places
        else:
            for place in places:
                place_activities = set(json.loads(place[8]))
                if len(activities_set.intersection(place_activities)) > 0:
                    return_places.append(place)
        c.close()

        print(len(return_places))
        json_to_be_returned = json.dumps(return_places, indent=2)

        return json_to_be_returned

    else:
        response["message"] = "nobody's logged in"
        response["success"] = 1
        return json.dumps(response)




if __name__ == '__main__':
    app.run(debug=True);