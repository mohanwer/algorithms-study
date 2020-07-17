# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    start_g = 0
    end_g = graph[-2][-1]
    possibles = []

    def dfs(v, path, n):
        nonlocal graph, possibles, end_g
        print(path)
        v[n] = True
        for i in graph[n]:
            if not v[i]:
                if i == end_g:
                    possibles.append(path + [i])
                    return
                dfs(visited, path + [i], i)

    visited = [False] * len(graph)
    dfs(visited, [start_g], start_g)
    return possibles

print(allPathsSourceTarget([[1,2],[3],[3],[]]))