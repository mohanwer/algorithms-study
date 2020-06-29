# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i -1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right] + nums[i]
            if total < 0 or (left > i + 1 and nums[left] == nums[left - 1]):
                left += 1
            elif total > 0 or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1




vals = [-1,0,1,2,-1,-4]

print(threeSum(vals))