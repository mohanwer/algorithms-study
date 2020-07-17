from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = set()
        max_o = []
        for i in range(len(nums)):
            q.add(max(max_o))
            if len(q) >= k:
                q.pop()
            max_o.append(max(q))

        return max_o
