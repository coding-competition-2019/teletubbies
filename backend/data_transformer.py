import json

#street passed as string
def get_coordinates(street):
    coordinate_X = 0
    coordinate_Y = 0

    #assign float values into coordinate_X and coordinate_Y - thats all
    return coordinate_X, coordinate_Y



with open("places.json", "r", encoding="utf8") as f:
    data = json.loads(f.read())

print(type(data))
print(type(data["places"]))
print(type(data["places"][0]))

for place in data["places"]:
    address = place["address"]
    street = address["street"]
    coordinate_X, coordinate_Y = get_coordinates(street)
    place["coordinate_X"] = coordinate_X
    place["coordinate_Y"] = coordinate_Y

with open("places_transformed.json", "w", encoding="utf8") as f:
    json.dump(data, f, indent=2)

