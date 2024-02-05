# Good for next or last greatest/smallest value.

arr = [4, 1, 2, 5]

q = []

for n in arr:
    while q and q[-1] > n:
        node = q.pop()
    q.append(n)

assert q == [1, 2, 5]