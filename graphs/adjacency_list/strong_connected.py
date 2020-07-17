# https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/

from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, visited, v):
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.dfs(visited, u)

    def dfs_start(self):
        visited = {k: False for k in self.graph.keys()}
        start = list(self.graph.keys())[0]
        self.dfs(visited, start)
        return {k: True for k in self.graph.keys()} == visited

    def reverse(self):
        r_g = Graph()
        for i in self.graph:
            for j in self.graph[i]:
                r_g.add_edge(j, i)
        return r_g

    def is_sc(self):
        if self.dfs_start():
            r = self.reverse()
            if r.dfs_start():
                return True
        return False


g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)
g1.add_edge(2, 4)
g1.add_edge(4, 2)
g1.add_edge(17, 1)
g1.add_edge(1, 17)
print ("Yes") if g1.is_sc() else print("No")
#
# g2 = Graph()
# g2.add_edge(0, 1)
# g2.add_edge(1, 2)
# g2.add_edge(2, 3)
# print ("Yes") if g2.is_sc() else print("No")