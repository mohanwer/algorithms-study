# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
import random

def findKthLargest(nums: List[int], k: int) -> int:
    def select(lst, l, r, index):
        if r == l:
            return lst[l]

        pv = random.randint(l, r)
        lst[pv], lst[l] = lst[l], lst[pv]
        i = l
        for j in range(l + 1, r + 1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[l], lst[i] = lst[i], lst[l]
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i - 1, index)
        else:
            return select(lst, i + 1, r, index)

    if nums is None or len(nums) < 1:
        return None
    return select(nums, 0, len(nums) - 1, len(nums) - k)