# https://leetcode.com/problems/two-sum/submissions/

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    h = {}
    for i in range(len(nums)):
        s = nums[i]
        find = target - s
        if h.get(find) is None:
            h[s] = i
        else:
            return [h[find], i]

q = [3, 2, 4]
z = twoSum(q, 6)