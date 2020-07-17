
def longestPalindrome(s: str) -> str:
    if len(s) < 1:
        return s
    biggest = s[0]

    def scan(l, r):
        nonlocal s, biggest
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        biggest = max(s[l+1:r], biggest, key=len)

    for i in range(len(s)):
        scan(i, i)
        scan(i, i + 1)

    return biggest


print(longestPalindrome("cbbd"))