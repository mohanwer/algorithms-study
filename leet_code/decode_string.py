def decodeString(s):
    stack = []
    stack.append([[], 1])
    num = []
    for ch in s:
        if ch.isdigit():
            num.append(ch)
        elif ch == '[':
            stack.append([[], int("".join(num))])
            num = []
        elif ch == ']':
            st, k = stack.pop()
            stack[-1][0].extend(st * k)
        else:
            stack[-1][0].append(ch)
    return "".join(stack[0][0])

print(decodeString("3a2[bc]"))

