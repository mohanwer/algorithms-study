# https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/

from collections import defaultdict


class Graph():

    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, src, dest, weight):
        self.edges[src].append(dest)
        self.edges[dest].append(src)
        self.weights[(src, dest)] = weight
        self.weights[(dest, src)] = weight

    def djisktra(self, initial, end):
        shortest_paths = {v[0]: (v[1], float('inf')) for i, v in enumerate(self.weights)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = self.edges[current_node]
            weight_current = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.weights[(current_node, next_node)] + weight_current
                if shortest_paths[next_node][1] > weight:
                    shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return None
            current_node = min(next_destinations, key=lambda x: next_destinations[x][1])

        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        path = path[::-1]
        return path

graph = Graph()

edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
]

for edge in edges:
    graph.add_edge(*edge)

z = graph.djisktra('X', 'Y')