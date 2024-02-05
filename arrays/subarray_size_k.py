#  https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

from typing import List

def subarray_size_key(arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i-1]
        arr = [0] + arr
        t = 0
        for i in range(k, n+1):
            _avg = (arr[i] - arr[i-k]) // k
            if _avg >= threshold:
                t += 1
        return t

assert subarray_size_key([2,2,2,2,5,5,5,8], 3, 4) == 3