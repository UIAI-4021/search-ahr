class Node:
    def __init__(self, data):
        self.name = data
        self.neighbors = {}

    def add_neighbor(self, node, edge):
        self.neighbors[node] = edge


class Graph:
    def __init__(self):
        self.vertices_num = 0
        self.vertices = []

    def check_vertex(self, data):
        for node in self.vertices:
            if checkValues(node.data, data):
                return node

        self.vertices_num += 1
        node = Node(data)
        self.vertices.append(node)
        return node

    def add_edge(self, edge, source_data, destination_data):
        node1 = self.check_vertex(source_data)
        node2 = self.check_vertex(destination_data)

        node1.add_neighbor(node2, edge)


def checkValues(data1, data2):
    if data1.airport == data2.airport and data1.city == data2.city and data1.latitude == data2.latitude \
            and data1.longitude == data2.longitude and data1.country == data2.country:
        return True
    return False
