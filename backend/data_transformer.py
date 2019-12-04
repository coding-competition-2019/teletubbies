import json, googlemaps

#street passed as string
def get_coordinates(street):
    
    gmaps_key = googlemaps.Client(key = "AIzaSyAVsQFt2JPrScp3gzgvu4FwnCGxH8mvmpw")

    geocode_res = gmaps_key.geocode(street)
    
    try:
        coordinate_X = geocode_res[0]["geometry"]["location"]["lat"]
        coordinate_Y = geocode_res[0]["geometry"]["location"]["lng"]
    except:
        coordinate_X = 0
        coordinate_Y = 0
        #invalid value


    #assign float values into coordinate_X and coordinate_Y - thats all
    return coordinate_X, coordinate_Y



with open("places.json", "r", encoding="utf8") as f:
    data = json.load(f)


counter = 0

for place in data["places"]:
    print(counter)
    counter += 1
    address = place["address"]
    street = address["street"]
    coordinate_X, coordinate_Y = get_coordinates(street)
    place["coordinate_X"] = coordinate_X
    place["coordinate_Y"] = coordinate_Y

with open("places_transformed.json", "w", encoding="utf8") as f:
    json.dump(data, f)

