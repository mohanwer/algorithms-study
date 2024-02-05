from typing import List
import collections

def sub_array_equals_k(nums: List[int], k: int):
    prefix_sum = 0
    prev_sum = collections.defaultdict(int)
    prev_sum[0] = 1
    sub_array_cnts = 0

    for n in nums:
        prefix_sum += n
        sub_array_cnts += prev_sum[prefix_sum - k]
        prev_sum[prefix_sum] += 1

    return sub_array_cnts

res = sub_array_equals_k([1,2,3], 3)
assert res == 2

