import networkx as nx
import heapq


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {}
        self.previous_airports = {}

    def find_shortest_path(self, start, end):
        # Initialize distances
        self.distances = {airport: float('inf') for airport in self.graph.nodes}
        self.distances[start] = 0

        priority_queue = [(0, start)]
        self.previous_airports = {}

        while priority_queue:
            current_distance, current_airport = heapq.heappop(priority_queue)

            if current_airport == end:
                path = []
                while current_airport:
                    path.insert(0, current_airport)
                    current_airport = self.previous_airports.get(current_airport)
                return path, self.distances[end]

            if self.distances[current_airport] < current_distance:
                continue

            for neighbor in self.graph.neighbors(current_airport):
                total_distance = current_distance + self.graph[current_airport][neighbor]['distance']
                if total_distance < self.distances[neighbor]:
                    self.distances[neighbor] = total_distance
                    self.previous_airports[neighbor] = current_airport
                    heapq.heappush(priority_queue, (total_distance, neighbor))

        return None, float('inf')  # it means that the distance to a particular airport is undefined until a valid path is
    # found.



