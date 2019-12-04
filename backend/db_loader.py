import json
import sqlite3

with open("places_transformed.json", "r", encoding="utf8") as f:
    data = json.load(f)


db = sqlite3.connect("McKinsey.db")
query = "insert into Places values (?,?,?,?,?,?,?)"

