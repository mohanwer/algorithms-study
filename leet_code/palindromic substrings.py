
def countSubstrings(s: str) -> int:
    drones = 0

    def find_palin(i: int):
        nonlocal s, drones
        left = i // 2
        right = (i + 1) // 2
        while left >= 0 and right < len(s) and s[left] == s[right]:
            drones += 1
            left -= 1
            right += 1

    for i in range(2*len(s)-1):
        find_palin(i)
    return drones

print(countSubstrings("aaa"))
