# https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/

from collections import defaultdict

class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, u, visited):
        visited[u] = True
        for i in range(self.graph[u]):
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self):
        visited = [False] * self.v
        self.dfs_util(0, visited)
        if all(v == True for v in visited):
            return True
        return False

    def reverse(self):
        g = Graph(self.v)
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def is_strong_connected(self):
        if self.dfs():
            g = self.reverse()
            if g.dfs():
                return True
        return False

g1 = Graph(5)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)
g1.add_edge(2, 4)
g1.add_edge(4, 2)
print ("Yes") if g1.is_strong_connected() else print("No")

g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
print ("Yes") if g2.is_strong_connected() else print("No")