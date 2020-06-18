# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[[0] * (vertices - 1)] * (vertices - 1)]

    def print_solution(self, dist):
        for node in range(self.V):
            print(node, "t", dist[node])

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        spt = [False] * self.V

        for _ in range(self.V):
            min = float('inf')
            u = 0
            for i, v in enumerate(dist):
                if not spt[i] and min > v:
                    min = v
                    u = i
            spt[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
