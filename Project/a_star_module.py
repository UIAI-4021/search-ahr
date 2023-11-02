from graph_module import *
from math import sin, cos, asin, sqrt, radians


def get_gn(edge):
    gn = edge.price * 2 + edge.distance
    return gn


def heuristic(key, destination):
    source_lat = radians(key.latitude)
    destination_lat = radians(destination.latitude)
    source_long = radians(key.longitude)
    destination_long = radians(destination.longitude)

    lat_difference = destination_lat - source_lat
    long_difference = destination_long - source_long

    a = sin(lat_difference / 2) ** 2 + cos(source_lat) * cos(destination_lat) * sin(long_difference / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371
    return distance
