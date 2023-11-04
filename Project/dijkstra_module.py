import heapq
from graph_module import *


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {}
        self.previous_airports = {}

    def find_shortest_path(self, start, end):
        # Initialize distances
        self.distances = {node.data.airport: float('inf') for node in self.graph.vertices}
        self.distances[start] = 0

        start_node = self.graph.get_vertex(start)
        priority_queue = [(0, start_node)]
        self.previous_airports = {}

        while priority_queue:
            current_distance, current_airport = heapq.heappop(priority_queue)

            if current_airport.data.airport == end:
                path = []
                while current_airport:
                    path.insert(0, current_airport.data.airport)
                    current_airport = self.previous_airports.get(current_airport)
                return path, self.distances[end]

            if self.distances[current_airport.data.airport] < current_distance:
                continue

            for neighbor, value in current_airport.neighbors.items():
                total_distance = current_distance + value.distance
                if total_distance < self.distances[neighbor.data.airport]:
                    self.distances[neighbor.data.airport] = total_distance
                    self.previous_airports[neighbor] = current_airport
                    heapq.heappush(priority_queue, (total_distance, neighbor))

        return None, float('inf')
        # it means that the distance to a particular airport is undefined until a valid path is
    # found.