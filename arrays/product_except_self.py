from typing import List

nums = [1,2,3,4]

def product(nums: List[int]) -> List[int]:
    n = len(nums)
    _copy = [0]*n
    l, r, ans = _copy, _copy[:], _copy[:]
    l[0] = r[-1] = 1

    for i in range(1, n):
        l[i] = l[i-1] * nums[i-1]

    for i in reversed(range(n-1)):
        r[i] = r[i+1] * nums[i+1]

    for i,(l,r) in enumerate(zip(l, r)):
        ans[i] = l * r

    return ans

res = product(nums)
assert res == [24,12,8,6]
