# https://leetcode.com/problems/01-matrix/

from typing import List

def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    from collections import deque
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(i2, j2):
        nonlocal offsets, matrix
        queue = deque([(i2, j2, 1)])
        visited = set()
        while queue:
            y, x, d = queue.popleft()
            for offset in offsets:
                x2, y2 = offset[0] + x, offset[1] + y
                if x2 < 0 or y2 < 0:
                    continue
                if x2 >= len(matrix[0]) or y2 >= len(matrix):
                    continue
                if (y2, x2) not in visited and matrix[y2][x2] == 0:
                    return d
                visited.add((y2, x2))
                queue.append((y2, x2, d+1))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                answer = bfs(i, j)
                matrix[i][j] = answer


q = [[0,0,0],
 [0,1,0],
 [1,1,1]]
updateMatrix(q)