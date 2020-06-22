from typing import List


def orangesRotting(grid: List[List[int]]) -> int:

    rottens = set()
    goods = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            orange = grid[i][j]
            if orange == 1:
                goods.add((i, j))
            elif orange == 2:
                rottens.add((i, j))

    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    more_found = True
    counter = 0
    rotten_current = [rotten for rotten in rottens]
    while more_found:
        more_found = False
        prev = counter
        new_rotten = set()
        for rotten in rotten_current:
            for offset in offsets:
                x_spot = offset[1] + rotten[1]
                y_spot = offset[0] + rotten[0]
                if x_spot >= 0 and x_spot <= len(grid[0]) and y_spot >= 0 and y_spot <= len(grid) and (x_spot, y_spot) in goods:
                    new_rotten.add((x_spot, y_spot))
                    goods.remove((x_spot, y_spot))
                    more_found = True
                    if prev == counter:
                        counter += 1
        rotten_current = new_rotten
    if len(goods) > 0:
        return -1
    return counter

question = [[1],[2],[1],[2]]
answer = orangesRotting(question)
