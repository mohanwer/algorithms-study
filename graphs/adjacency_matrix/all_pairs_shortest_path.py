
"""
https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
https://github.com/keon/algorithms/blob/master/algorithms/graph/all_pairs_shortest_path.py

Given a n*n adjacency array.
it will give you all pairs shortest path length.
use deepcopy to preserve the original information.

a = [
    [0, 0.1, 0.101, 0.142, 0.277],
    [0.465, 0, 0.191, 0.192, 0.587],
    [0.245, 0.554, 0, 0.333, 0.931],
    [1.032, 0.668, 0.656, 0, 0.151],
    [0.867, 0.119, 0.352, 0.398, 0]
]

result =
[
    [0, 0.1, 0.101, 0.142, 0.277],
    [0.436, 0, 0.191, 0.192, 0.34299999999999997],
    [0.245, 0.345, 0, 0.333, 0.484],
    [0.706, 0.27, 0.46099999999999997, 0, 0.151],
    [0.5549999999999999, 0.119, 0.31, 0.311, 0]
]

Time complexity : O(V^3)
"""

import copy

def all_pairs_shortest_path(adj_matrix):
    new_arr = copy.deepcopy(adj_matrix)
    size = len(adj_matrix)

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if new_arr[i][j] > new_arr[i][k] + new_arr[k][j]:
                    new_arr[i][j] = new_arr[i][k] + new_arr[k][j]