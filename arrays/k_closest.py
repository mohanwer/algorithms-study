
arr = [1, 2, 3, 4, 5]

def k_closest(arr, k, x):
    sorted_arr = sorted(arr, key=lambda y: abs(x - y))
    res = sorted_arr[:k]
    return sorted(res)

assert k_closest(arr, 4, 3) == [1,2,3,4]