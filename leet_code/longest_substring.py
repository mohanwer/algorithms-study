# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2961/

def lengthOfLongestSubstring(s: str) -> int:
    dct = {}
    max_so_far = curr_max = start = 0
    for index, i in enumerate(s):
        if i in dct and dct[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            start = dct[i] + 1
        else:
            curr_max += 1
        dct[i] = index
    return max(max_so_far, curr_max)

print(lengthOfLongestSubstring("abb"))