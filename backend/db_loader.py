import json
import sqlite3

with open("places_transformed.json", "r", encoding="utf8") as f:
    data = json.load(f)


db = sqlite3.connect("McKinsey.db")
query = "insert into Places(name,url,street,zipcode,city, coordinate_x, coordinate_y, activities) values (?,?,?,?,?,?,?,?)"

for place in data["places"]:
    column = [str(place["name"]), str(place["url"]), str(place["address"]["street"]), str(place["address"]["zipCode"]), str(place["address"]["city"]), str(place["coordinate_X"]), str(place["coordinate_Y"]), json.dumps(list(place["activities"]))]
    print(column)
    c = db.cursor()
    c.execute(query, column)
    db.commit()
    c.close()


