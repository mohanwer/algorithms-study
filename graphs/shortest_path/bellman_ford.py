# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
# https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
# https://www.youtube.com/watch?v=FtN3BYH2Zes&t=388s

# finds shortest paths from src to all vertices in given graph even if it contains negative weights
# O(VE) complexity
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        visited = [False] * n
