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


def a_star_search(graph, source, destination):
    startNode = graph.get_vertex(source)
    stopNode = graph.get_vertex(destination)

    if startNode is None or stopNode is None:
        print("source or destination not found")

    frontier = [startNode]
    visited = []

    distances = {startNode: 0}
    answer = {startNode: None}

    while len(frontier) > 0:
        lowest = frontier[0]

        for i in range(1, len(frontier)):
            fn1 = distances[frontier[i]] + heuristic(frontier[i].data, stopNode.data)
            fn2 = distances[lowest] + heuristic(lowest.data, stopNode.data)
            if fn1 < fn2:
                lowest = frontier[i]

        if lowest != stopNode:
            for (key, value) in lowest.neighbors.items():
                fnLowest = distances[lowest] + get_gn(value)
                if key in distances.keys():
                    if distances[key] > fnLowest:
                        answer[key]=lowest
                        distances[key] = fnLowest
                        if key in visited:
                            visited.remove(key)
                            frontier.append(key)
                else:
                    frontier.append(key)
                    distances[key] = fnLowest
                    answer[key] = lowest

        visited.append(lowest)
        frontier.remove(lowest)
