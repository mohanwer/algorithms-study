from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height)-1
    area = 0
    while left < right:
        curr_area = (right - left) * min(height[right], height[left])
        area = max(area, curr_area)
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    return area

vals = []
print(maxArea(vals))