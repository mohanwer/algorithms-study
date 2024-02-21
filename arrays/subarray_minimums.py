from typing import List

input = [3, 1, 2, 4]


def sum_of_subarray_minimums(arr: List[int]) -> int:
    stack = []
    t = 0

    for i in range(len(arr) + 1):
        while stack and (i == len(arr) or arr[stack[-1]] > arr[i]):
            mid = stack.pop()
            l = -1 if not stack else stack[-1]
            left = mid - l
            right = i - mid
            t += left * right * arr[mid]
        stack.append(i)

    return t


assert sum_of_subarray_minimums(input) == 17
