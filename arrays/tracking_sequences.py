# use input array and it's position to track whether a value is found or not.
from typing import List

nums = [4,3,2,7,8,2,3,1]

def find_missing_numbers(nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            v = abs(nums[i])
            if nums[v-1] > 0:
                nums[v-1] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


assert find_missing_numbers(nums) == [5, 6]
