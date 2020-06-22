from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = defaultdict(list)

    def add_edge(self, u, v):
        self.vertices[u].append(v)

    def bfs(self, src):
        visited = [False] * len(self.vertices)
        queue = [src]
        while queue:
            node = queue.pop(0)
            for vertex in self.vertices[node]:
                if not visited[vertex]:
                    queue.append(vertex)
                    visited[vertex] = True