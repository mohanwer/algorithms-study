# https://leetcode.com/problems/walls-and-gates/
from typing import List
from collections import deque

def wallsAndGates(rooms: List[List[int]]) -> None:
    if len(rooms) == 0:
        return []
    offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    y_len = len(rooms) - 1
    x_len = len(rooms[0]) - 1

    def bfs(count, i, j):
        nonlocal offsets, rooms
        queue = deque([])
        queue.append((i, j, count))
        visited = set()
        while queue:
            i2, j2, d = queue.popleft()
            for offset in offsets:
                x, y = offset[0] + i2, offset[1] + j2
                if x > x_len or x < 0 or y > y_len or y < 0 or rooms[y][x] in [0, -1] or (x, y) in visited:
                    continue
                visited.add((x, y))
                rooms[y][x] = min(d, rooms[y][x])
                queue.append((x, y, d+1))

    for u in range(len(rooms)):
        for v in range(len(rooms[0])):
            if rooms[u][v] == 0:
                bfs(1, v, u)


path = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
wallsAndGates(path)