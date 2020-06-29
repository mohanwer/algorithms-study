import random

def quicksort(items):

    def sort(lst, l, r):
        if r <= l:
            return

        pv = random.randint(l, r)
        lst[pv], lst[l] = lst[l], lst[pv]
        i = l
        for j in range(l+1, r+1):
            if lst[j] > lst[l]:
                i+=1
                lst[i], lst[j] = lst[j], lst[i]
        lst[l], lst[i] = lst[i], lst[l]
        sort(lst, l, i -1 )
        sort(lst, i + 1, r)

    if items is None or len(items) < 2:
        return
    sort(items, 0, len(items) - 1)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quicksort(arr)
print(arr)