class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, node, edge):
        self.neighbors[node] = edge


class Graph:
    def __init__(self):
        self.vertices_num = 0
        self.vertices = []

    def check_vertex(self, name):
        for node in self.vertices:
            if node.name == name:
                return node

        self.vertices_num += 1
        node = Node(name)
        self.vertices.append(node)
        return node

    def add_edge(self, edge, name1, name2):
        node1 = self.check_vertex(name1)
        node2 = self.check_vertex(name2)

        node1.add_neighbor(node2, edge)
        node2.add_neighbor(node1, edge)
