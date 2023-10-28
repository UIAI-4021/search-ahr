class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, node, edge):
        self.neighbors[node] = edge
