# https://leetcode.com/problems/trapping-rain-water/solution/

from typing import List


def trap(height: List[int]) -> int:
    left_max_lst = [0] * len(height)
    right_max_lst = [0] * len(height)
    water = [0] * len(height)
    max_left = 0
    max_right = 0
    for i in range(len(height)):
        max_left = max(height[i], max_left)
        left_max_lst[i] = max_left

    for i in range(len(height)-1, -1, -1):
        max_right = max(height[i], max_right)
        right_max_lst[i] = max_right

    for i in range(len(height)):
        mini = min(left_max_lst[i], right_max_lst[i])
        water[i] = mini - height[i]

    return sum(water)


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))