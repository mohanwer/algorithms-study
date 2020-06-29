# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/

def myAtoi(str: str) -> int:
    int_max = 2**31-1
    int_min = -2**31
    str = str.lstrip()
    ans = ""
    for i, v in enumerate(str):
        if 'a' <= v <= 'z' or (v == ' ' and len(ans) > 0):
            break
        elif v == ' ':
            continue
        else:
            ans = ans + v
    if not len(ans):
        return 0
    if ans == "-" or ans == "+" or ans.startswith("+-") or ans.startswith("-+"):
        return 0
    val = float(ans)
    if val > int_max:
        return int_max
    elif val < int_min:
        return int_min
    return int(val)

print(myAtoi("   +0 123"))