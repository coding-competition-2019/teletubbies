from math import sin, cos, sqrt, atan2, radians



def distance(lat1, lon1, lat2, lon2):
    r = 6378.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1

    a = sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    dist = r * c

    return dist

def distance_vector(lat1, lon1, lat2, lon2):
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    dist = 111 * sqrt(d_lat**2 + d_lon**2)

    return dist

print(distance(50.210067, 13.316010, 50.207336, 13.321550))
print(distance_vector(50.210067, 13.316010, 50.207336, 13.321550))
