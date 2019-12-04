import json

with open("places.json") as f:
    data = json.load(f)

for place in data["places"]:

