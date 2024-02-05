
arr = [1,2,3,4,5]

def k_closest(arr, k, x):
    pre = sum(arr[:k-1])
    ans = [10**9, -1]
    for i in range(k-1, len(arr)):
        pre += arr[i]
        pre -= arr[i - k]
        v = abs(pre // k - x)
        ans = min(ans, [v, i])

    idx = ans[1]
    return arr[idx-k:idx]

assert k_closest(arr, 4) 