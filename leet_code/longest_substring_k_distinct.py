from collections import OrderedDict


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    n = len(s)
    if k == 0 or n == 0:
        return 0

    left = right = 0

    hash_m = OrderedDict()

    max_len = 1

    while right < n:
        character = s[right]
        if character in hash_m:
            del hash_m[character]
        hash_m[character] = right
        right += 1

        if len(hash_m) == k + 1:
            _, del_idx = hash_m.popitem(last=False)
            left = del_idx + 1
        max_len = max(max_len, right - left)
    return max_len