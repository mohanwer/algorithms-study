from typing import List


def numIslands(grid: List[List[str]]) -> int:
    y_len = len(grid) - 1
    if y_len == -1:
        return 0
    x_len = len(grid[0]) - 1
    if x_len == -1:
        return 0
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    islands = 0


    def dfs(visited, i, j):
        nonlocal offsets, grid
        if visited[i][j]:
            return
        visited[i][j] = True
        for offset in offsets:
            x, y = offset[0] + j, offset[1] + i
            if x <= x_len and y <= y_len and x >= 0 and y >= 0 and grid[y][x] == "1":
                dfs(visited, y, x)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == "1":
                islands += 1
                dfs(visited, i, j)

    return islands

grid = []
z = numIslands(grid)